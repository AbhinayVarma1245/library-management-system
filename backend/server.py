from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db, Book, BorrowHistory
from validators import validate_book_data, validate_borrower_name
from datetime import datetime, timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)
db.init_app(app)

@app.route("/api/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "isbn": b.isbn,
        "category": b.category,
        "publication_year": b.publication_year,
        "available": b.available
    } for b in books])

@app.route("/api/books", methods=["POST"])
def add_book():
    data = request.json

    valid, error = validate_book_data(data)
    if not valid:
        return jsonify({"error": error}), 400

    if Book.query.filter_by(isbn=data["isbn"]).first():
        return jsonify({"error": "Book with this ISBN already exists"}), 409

    book = Book(**data)
    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book added successfully"}), 201

@app.route("/api/books/<book_id>/borrow", methods=["POST"])
def borrow_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    if not book.available:
        return jsonify({"error": "Book is not available"}), 400

    data = request.json
    valid, error = validate_borrower_name(data.get("borrower_name"))
    if not valid:
        return jsonify({"error": error}), 400

    book.available = False

    history = BorrowHistory(
        book_id=book.id,
        borrower_name=data["borrower_name"]
    )

    db.session.add(history)
    db.session.commit()

    return jsonify({"message": "Book borrowed successfully"})

@app.route("/api/books/<book_id>/return", methods=["POST"])
def return_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    book.available = True

    history = BorrowHistory.query.filter_by(book_id=book_id, returned_at=None).first()
    if history:
        history.returned_at = datetime.now(timezone.utc)

    db.session.commit()

    return jsonify({"message": "Book returned successfully"})

@app.route("/api/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted successfully"})

from asgiref.wsgi import WsgiToAsgi
flask_app = app
app = WsgiToAsgi(flask_app)

if __name__ == "__main__":
    with flask_app.app_context():
        db.create_all()
    flask_app.run(host="0.0.0.0", port=8001, debug=True)
