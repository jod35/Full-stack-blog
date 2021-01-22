from flask import Blueprint,request
from flask_restx import Api,Resource,fields
from .models import User,Post,Comment


resources=Blueprint('api',__name__)

api=Api(resources)

user_model=api.model(
    "User",
    {   "id":fields.Integer(),
        "username":fields.String(),
        "email":fields.String(),
        "password":fields.String(),
        "date_joined":fields.DateTime(dt_format='rfc822'),
    }
)

post_model=api.model(
    'Post',
    {   'id':fields.Integer(),
        'title':fields.String(),
        'body':fields.String(),
        'user_id':fields.Integer(),
        'date_added':fields.DateTime(dt_format='rfc822')
    }
)

comment_model=api.model(
    'Comment',
    {
        "id":fields.Integer(),
        "body":fields.String(),
        "date_added":fields.DateTime(dt_format='rfc822'),
        "user_id":fields.Integer()
    }
)


@api.route('/users')
class Users(Resource):

    @api.marshal_with(user_model,envelope='users')
    def get(self):
        users = User.get_all()

        return users