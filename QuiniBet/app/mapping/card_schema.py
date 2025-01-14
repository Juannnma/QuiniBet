from app.models.card import Card
from marshmallow import validate, fields, Schema, post_load

class CardSchema(Schema):
    code_card = fields.Integer(dump_only=True)
    numbers = fields.String(required=True)
    date = fields.String(required=True)
    time = fields.String(required=True)

    @post_load
    def make_card(self, data, **kwargs):
        return Card(**data)