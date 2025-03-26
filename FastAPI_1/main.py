from fastapi import FastAPI, HTTPException, status
from typing import List

from library.models import Book
from library.schemas import BookSchema
from library.services import book_service

app = FastAPI()


@app.get("/books", response_model=List[Book])
async def read_books():
    return book_service.get_all_books()


@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    book = book_service.get_book_by_id(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookSchema):
    new_book = Book(id=0, title=book.title, author=book.author, year=book.year)
    try:
        created_book = book_service.add_book(new_book)
        return created_book
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve)
        )


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_route(book_id: int):
    if not book_service.delete_book(book_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return None