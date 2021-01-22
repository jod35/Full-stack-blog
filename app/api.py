from flask import Blueprint,request
from flask_restx import Api,Resource,fields
from .models import User,Post,Comment
from werkzeug.security import generate_password_hash,check_password_hash
from .utils import db

resources=Blueprint('api',__name__)

api=Api(resources,
        title='Blog Api',
        description="A REST service for a blogging application",
        default="Endpoints",
        default_label="API Endpoints"
     )

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
        '''Get all users '''
        users = User.get_all()

        return users
    
    @api.marshal_with(user_model,envelope='user')
    @api.expect(user_model)
    def post(self):
        ''' Create a new User or sign up '''

        data=request.get_json()

        new_user=User(
                      username=data.get('username'),
                      email=data.get('email'),
                      password=generate_password_hash(data.get('password'))
                )
        new_user.save()

        return new_user


@api.route('/user/<int:id>')
class UserResource(Resource):

    @api.marshal_with(user_model)
   
    def get(self,id):
        ''' Get a user by ID'''
        user=User.get_by_id(id)

        return user

    @api.marshal_with(user_model)
    @api.expect(user_model)
    def put(self,id):
        ''' Update all user info '''

        user=User.get_by_id(id)

        data=request.get_json()

        user.username=data.get('username')

        user.email=date.get('email')

        db.session.commit()

        return user

    @api.marshal_with(user_model)
    def delete(self,id):
        ''' Delete a user with ID '''
        user=User.get_by_id(id)

        user.delete()

        return user



@api.route('/posts')
class Posts(Resource):
    @api.marshal_with(post_model,envelope='posts')
    def get(self):
        ''' Get all posts'''
        
        posts=Post.get_all()

        return posts

    @api.marshal_with(post_model,envelope='post')
    @api.expect(post_model)
    def post(self):
        ''' Create a new post '''

        data=request.get_json()

        new_post= Post(
            title=data.get('title'),
            body=data.get('body')
        ) 

        new_post.save()

        return new_post




@api.route('/post/<int:id>')
class PostResource(Resource):
    @api.marshal_with(post_model)
    def get(self,id):
        '''Get a post by ID '''
        post=Post.get_by_id(id)

        return post

    
    @api.marshal_with(post_model)
    @api.expect(post_model)
    def put(self,id):
        '''Update a post with an ID '''
        post=Post.get_by_id(id)

        data=request.get_json()

        post.title=data.get('title')

        post.body=data.get('body')

        db.session.commit()

        return post

    @api.marshal_with(post_model)
    def delete(self,id):
        post=Post.get_by_id(id)

        post.delete()

        return post
    

@api.route('/comments')
class Comments(Resource):

    @api.marshal_with(comment_model)
    def get(self):
        ''' Get all comments '''
        comments=Comment.get_all()

        return comments

    @api.marshal_with(comment_model)
    @api.expect(comment_model)
    def post(self):
        ''' Create a new comment '''

        data=request.get_json()

        new_comment=Comment(
            body=data.get('body')
        )

        new_comment.save()

        return new_comment


@api.route('/comment/<int:id>')
class CommentResource(Resource):

    @api.marshal_with(comment_model)
    def get(self,id):
        '''Get a comment with an ID '''
        comment=Comment.get_by_id(id)

        return comment
    
    @api.marshal_with(comment_model)
    def put(self):
        ''' Update a comment with an ID'''
        comment=Comment.get_by_id(id)

        data=request.get_json()

        comment.body=data.get('body')

        db.session.commit()

        return comment

    
    @api.marshal_with(comment_model)
    def delete(self):
        comment=Comment.get_by_id(id)

        comment.delete()

        return comment