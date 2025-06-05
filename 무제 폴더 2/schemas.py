from marshmallow import Schema, fields

class LibraryItemSchema(Schema):
    title = fields.String(required=True)
    author = fields.String(required=True)
    id = fields.Integer(dump_only=True)