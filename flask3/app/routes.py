from flask import Flask, jsonify, request
from app.schemas import BookSchema
from app.services import get_books, get_book_by_id, add_book, delete_book

def register_routes(app: Flask):
    @app.route("/books", methods=["GET"])
    def get_books_route():
        try:
            page_size = int(request.args.get("page_size", 10))
            cursor = request.args.get("cursor")

            if page_size < 1:
                return jsonify({"message": "Page size must be greater than 0"}), 400

            books, next_cursor = get_books(page_size, cursor)
            response = {
                "books": books,
                "next_cursor": next_cursor
            }
            return jsonify(response)
        except ValueError:
            return jsonify({"message": "Page size must be an integer"}), 400

    @app.route("/books/<int:book_id>", methods=["GET"])
    def get_book_route(book_id):
        book = get_book_by_id(book_id)
        if book:
            return jsonify(book)
        return jsonify({"message": "Book not found"}), 404

    @app.route("/books", methods=["POST"])
    def create_book():
        schema = BookSchema()
        try:
            book_data = schema.load(request.get_json())
        except Exception as e:
            return jsonify({"message": str(e)}), 400

        new_book = add_book(book_data)
        return jsonify({"message": "Book created successfully", "book": new_book}), 201

    @app.route("/books/<int:book_id>", methods=["DELETE"])
    def delete_book_route(book_id):
        if delete_book(book_id):
            return jsonify({"message": "Book deleted successfully"}), 204
        return jsonify({"message": "Book not found"}), 404
