import React, { useEffect, useState } from "react";
import "./App.css";
import { getBooks, addBook, borrowBook, returnBook, deleteBook } from "./services/api";

function App() {
  const [books, setBooks] = useState([]);
  const [form, setForm] = useState({
    title: "",
    author: "",
    isbn: "",
    category: "",
    publication_year: ""
  });

  const loadBooks = async () => {
    const data = await getBooks();
    setBooks(data);
  };

  useEffect(() => {
    loadBooks();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addBook(form);
    setForm({ title: "", author: "", isbn: "", category: "", publication_year: "" });
    loadBooks();
  };

  return (
    <div className="container">
      <h1>Library Management System</h1>

      <form onSubmit={handleSubmit}>
        {Object.keys(form).map((key) => (
          <input
            key={key}
            placeholder={key.replace("_", " ")}
            value={form[key]}
            onChange={(e) => setForm({ ...form, [key]: e.target.value })}
            required
          />
        ))}
        <button type="submit">Add Book</button>
      </form>

      <div className="grid">
        {books.map((book) => (
          <div key={book.id} className="card">
            <h3>{book.title}</h3>
            <p><strong>Author:</strong> {book.author}</p>
            <p><strong>ISBN:</strong> {book.isbn}</p>
            <p><strong>Category:</strong> {book.category}</p>
            <p><strong>Year:</strong> {book.publication_year}</p>
            <p className={book.available ? "available" : "borrowed"}>
              {book.available ? "✅ Available" : "❌ Borrowed"}
            </p>

            {book.available ? (
              <button className="borrow-btn" onClick={() => { borrowBook(book.id, "User"); loadBooks(); }}>Borrow</button>
            ) : (
              <button className="return-btn" onClick={() => { returnBook(book.id); loadBooks(); }}>Return</button>
            )}

            <button className="delete-btn" onClick={() => { deleteBook(book.id); loadBooks(); }}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;