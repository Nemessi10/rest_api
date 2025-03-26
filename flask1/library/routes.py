from flask import Flask, jsonify, request
from library.schemas import BookSchema
from library.services import get_all_books, get_book_by_id, add_book, delete_book

def register_routes(app: Flask):
    @app.route("/books", methods=["GET"])
    def get_books():
        return jsonify(get_all_books())

    @app.route("/books/<int:book_id>", methods=["GET"])
    def get_book(book_id):
        book = get_book_by_id(book_id)
        if book:
            return jsonify(book)
        return jsonify({"message": "Book not found"}), 404

    @app.route("/books", methods=["POST"])
    def create_book():
        schema = BookSchema()
        try:
            book = schema.load(request.get_json()) # validate incoming data without id
        except Exception as e:
            return jsonify({"message": str(e)}), 400

        new_book = add_book(book) # add_book returns the new book with id
        return jsonify({"message": "Book created successfully", "book": new_book}), 201

    @app.route("/books/<int:book_id>", methods=["DELETE"])
    def delete_book_route(book_id):
        book = get_book_by_id(book_id)
        if not book:
            return jsonify({"message": "Book not found"}), 404

        delete_book(book_id)
        return jsonify({"message": "Book deleted successfully"}), 204

