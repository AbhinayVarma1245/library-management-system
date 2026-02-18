import uuid
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    history = db.relationship("BorrowHistory", backref="book", lazy=True)

class BorrowHistory(db.Model):
    __tablename__ = "borrow_history"

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    book_id = db.Column(db.String(36), db.ForeignKey("books.id"), nullable=False)
    borrower_name = db.Column(db.String(200), nullable=False)
    borrowed_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    returned_at = db.Column(db.DateTime, nullable=True)
