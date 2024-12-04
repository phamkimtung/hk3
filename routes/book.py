from flask import Blueprint, jsonify
from models.sach import Sach
from database import db

# Khởi tạo blueprint
book_routes = Blueprint('book_routes', __name__, url_prefix='/api')

@book_routes.route('/books', methods=['GET'])
def get_all_books():
    """API lấy tất cả sách."""
    books = Sach.query.all()
    return jsonify({
        "success": True,
        "data": [book.to_dict() for book in books]
    })

@book_routes.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    """API lấy sách theo ID."""
    book = Sach.query.get(book_id)
    if book:
        return jsonify({
            "success": True,
            "data": book.to_dict()
        })
    else:
        return jsonify({
            "success": False,
            "message": "Sách không tồn tại"
        }), 404
