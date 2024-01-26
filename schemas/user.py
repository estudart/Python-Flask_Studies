from marshmallow import Schema

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'first_name', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
