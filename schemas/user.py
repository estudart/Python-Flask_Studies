from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    email = fields.Str()
    password = fields.Str()

user_schema = UserSchema()
users_schema = UserSchema(many=True)
