from app.models.user import User
from marshmallow import fields, Schema, post_load

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    surname = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(load_only=True)
    data = fields.Dict(required=False)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)