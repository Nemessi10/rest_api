import copy

books_data = [
    {"id": 1, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
]

def get_all_books():
    return books_data

def get_book_by_id(book_id: int):
    for book in books_data:
        if book["id"] == book_id:
            return book
    return None

def add_book(book: dict):
    new_book = copy.deepcopy(book)
    new_book["id"] = max(book["id"] for book in books_data) + 1 if books_data else 1
    books_data.append(new_book)
    return new_book

def delete_book(book_id: int):
    global books_data
    books_data = [book for book in books_data if book["id"] != book_id]
