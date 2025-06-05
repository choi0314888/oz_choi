from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import LibraryItemSchema

blp = Blueprint("Library", __name__, description="도서관 API")

book_storage = []
book_index = 1

@blp.route("/library")
class LibraryCollection(MethodView):

    @blp.response(200, LibraryItemSchema(many=True))
    def list_books(self):
        return book_storage

    @blp.arguments(LibraryItemSchema)
    @blp.response(201, LibraryItemSchema)
    def create_book(self, data):
        global book_index
        data["id"] = book_index
        book_index += 1
        book_storage.append(data)
        return data

@blp.route("/library/<int:item_id>")
class LibraryItem(MethodView):

    @blp.arguments(LibraryItemSchema)
    @blp.response(200, LibraryItemSchema)
    def modify_book(self, update_data, item_id):
        for book in book_storage:
            if book["id"] == item_id:
                book.update(update_data)
                return book
        abort(404, message="해당 책을 찾을 수 없습니다.")

    @blp.response(204)
    def remove_book(self, item_id):
        global book_storage
        book_storage = [b for b in book_storage if b["id"] != item_id]
        return ""