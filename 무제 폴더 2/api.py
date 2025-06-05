from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

blp = Blueprint("Books", __name__, description="책 관리 API")

books = []
book_id_counter = 1

@blp.route("/books")
class BooksResource(MethodView):

    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_data):
        global book_id_counter
        new_data["id"] = book_id_counter
        book_id_counter += 1
        books.append(new_data)
        return new_data

@blp.route("/books/<int:book_id>")
class BookResource(MethodView):

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, updated_data, book_id):
        for book in books:
            if book["id"] == book_id:
                book.update(updated_data)
                return book
        abort(404, message="책을 찾을 수 없습니다.")

    @blp.response(204)
    def delete(self, book_id):
        global books
        books = [b for b in books if b["id"] != book_id]
        return ""