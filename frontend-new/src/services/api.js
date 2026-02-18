const BASE_URL = process.env.REACT_APP_BACKEND_URL;

export const getBooks = async () => {
  const res = await fetch(`${BASE_URL}/api/books`);
  return res.json();
};

export const addBook = async (bookData) => {
  const res = await fetch(`${BASE_URL}/api/books`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(bookData),
  });
  return res.json();
};

export const borrowBook = async (bookId, borrowerName) => {
  const res = await fetch(`${BASE_URL}/api/books/${bookId}/borrow`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ borrower_name: borrowerName }),
  });
  return res.json();
};

export const returnBook = async (bookId) => {
  const res = await fetch(`${BASE_URL}/api/books/${bookId}/return`, {
    method: "POST",
  });
  return res.json();
};

export const deleteBook = async (bookId) => {
  const res = await fetch(`${BASE_URL}/api/books/${bookId}`, {
    method: "DELETE",
  });
  return res.json();
};