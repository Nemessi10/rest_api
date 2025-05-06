from app.extensions import db
from app.models import Book
from sqlalchemy import desc

def get_books(page_size=10, cursor=None):
    query = Book.query.order_by(desc(Book.id))
    
    if cursor:
        last_book = Book.query.get(cursor)
        if last_book:
            query = query.filter(Book.id < last_book.id)
    
    books = query.limit(page_size + 1).all()
    
    has_more = len(books) > page_size
    books = books[:page_size]
    
    next_cursor = books[-1].id if books and has_more else None
    
    return [book.to_dict() for book in books], next_cursor

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
