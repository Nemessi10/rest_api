from app.extensions import db
from app.models import Book

def get_books(limit=10, offset=0):
    books = Book.query.limit(limit).offset(offset).all()
    return [book.to_dict() for book in books]

def get_book_by_id(book_id):
    book = Book.query.get(book_id)
    return book.to_dict() if book else None

def add_book(book_data):
    new_book = Book(**book_data)
    db.session.add(new_book)
    db.session.commit()
    return new_book.to_dict()

def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return True
    return False
