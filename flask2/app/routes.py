from flask import Flask, jsonify, request
from app.schemas import BookSchema
from app.services import get_books, get_book_by_id, add_book, delete_book

def register_routes(app: Flask):
    @app.route("/books", methods=["GET"])
    def get_books_route():
        try:
            limit = int(request.args.get("limit", 10))
            offset = int(request.args.get("offset", 0))

            if limit < 1 or offset < 0:
                return jsonify({"message": "Invalid pagination parameters"}), 400

            books = get_books(limit, offset)
            return jsonify(books)
        except ValueError:
            return jsonify({"message": "Limit and offset must be integers"}), 400

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
