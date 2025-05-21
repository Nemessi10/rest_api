from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException, status

from app import services
from app.schemas import Book, BookCreate

app = FastAPI()
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

@app.get("/")
async def root():
    return {"message": "Hi, welcome to the book API"}

@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate):
    return await services.create_book(book)

@app.get("/books", response_model=List[Book])
async def get_books():
    return await services.get_books()

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: str):
    book = await services.get_book(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str):
    deleted = await services.delete_book(book_id)
    if deleted:
        return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")