VALID_ISBN_LENGTHS = [10, 13]

def validate_book_data(data):
    required_fields = ["title", "author", "isbn", "category", "publication_year"]

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return False, f"{field} is required"

    isbn = str(data["isbn"]).strip()

    if not isbn.isdigit() or len(isbn) not in VALID_ISBN_LENGTHS:
        return False, "ISBN must be 10 or 13 digits"

    return True, None

def validate_borrower_name(name):
    if not name or not str(name).strip():
        return False, "Borrower name is required"

    if len(name.strip()) < 2:
        return False, "Borrower name must be at least 2 characters"

    return True, None
