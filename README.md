# Library Management System

A full-stack web application for managing a library's book inventory — built with Python/Flask, React, and SQLite.

## Tech Stack

- **Backend**: Python + Flask (REST API)
- **Frontend**: React
- **Database**: SQLite via Flask-SQLAlchemy
- **Other**: Flask-CORS, asgiref, uvicorn

## Features

- Add books with title, author, ISBN, category, and publication year
- View all books in a responsive card grid
- Borrow and return books (tracks availability)
- Delete books from the system
- Input validation on both frontend and backend
- Borrow history tracked in the database

## Project Structure

```
library-management-system/
├── backend/
│   ├── server.py        # Flask API routes
│   ├── database.py      # SQLAlchemy models (Book, BorrowHistory)
│   ├── validators.py    # Input validation logic
│   └── requirements.txt
└── frontend/
    ├── .env             # Backend URL config
    └── src/
        ├── App.js       # Main React component
        ├── App.css      # Styles
        └── services/
            └── api.js   # API call functions
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt
python server.py
```

Backend runs at `http://localhost:8001`

### Frontend Setup

Open a second terminal:

```bash
cd frontend
npm install
npm start
```

Frontend runs at `http://localhost:3000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books` | Get all books |
| POST | `/api/books` | Add a new book |
| POST | `/api/books/:id/borrow` | Borrow a book |
| POST | `/api/books/:id/return` | Return a book |
| DELETE | `/api/books/:id` | Delete a book |

## Key Technical Decisions

**SQLite for the database** — chosen for simplicity and zero-config setup. For production, this would be swapped for PostgreSQL.

**Validation in a separate module** — `validators.py` is isolated from route logic, making it easy to update rules (e.g. ISBN length) without touching the API layer.

**ISBN validation** — enforces 10 or 13 digit numeric ISBNs to prevent bad data entering the system.

**Flask-CORS** — enabled globally to allow the React frontend to communicate with the Flask backend during local development.

**BorrowHistory model** — borrow/return events are stored separately from the Book model, keeping concerns separated and allowing future audit/history features.

## Known Limitations & Future Improvements

- Authentication/authorization not implemented — any user can borrow or delete
- Borrower name is hardcoded as "User" in the frontend — should be a user input field
- SQLite is not suitable for concurrent production use — would migrate to PostgreSQL
- No pagination on the book list — could be slow with large datasets
- No unit tests currently — would add pytest coverage for validators and API routes

## AI Usage

Claude (claude.ai) was used during development to:
- Debug CORS and environment variable configuration issues
- Identify and fix validation error responses
- Improve frontend UI styling and card layout
- Generate the `.env` setup and project structure guidance

All AI-generated suggestions were reviewed, tested, and verified manually before being included.
