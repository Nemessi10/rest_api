import copy
from typing import List, Optional
from .models import Book

class BookService:
    def __init__(self):
        self.books_data = [
            Book(id=1, title="The Lord of the Rings", author="J.R.R. Tolkien", year=1954),
            Book(id=2, title="Pride and Prejudice", author="Jane Austen", year=1813),
            Book(id=3, title="1984", author="George Orwell", year=1949),
        ]

    def get_all_books(self) -> List[Book]:
        return self.books_data

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books_data if book.id == book_id), None)

    def add_book(self, book: Book) -> Book:
        new_book = copy.deepcopy(book)
        new_book.id = max(book.id for book in self.books_data) + 1 if self.books_data else 1
        self.books_data.append(new_book)
        return new_book

    def delete_book(self, book_id: int) -> bool:
        original_length = len(self.books_data)
        self.books_data = [book for book in self.books_data if book.id != book_id]
        return len(self.books_data) < original_length

book_service = BookService()