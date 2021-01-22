from .utils import db
from datetime import datetime


class User(db.Model):
    '''The user table '''
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.Text,nullable=False)
    date_joined=db.Column(db.DateTime(),default=datetime.utcnow)
    posts=db.relationship(
        'Post',backref='author',lazy=True
    )
    comments=db.relationship(
        'Comment',backref='author',lazy=True
    )
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password

    def __repr__(self):
        return f"< User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod 
    def get_all_desc(cls):
        return cls.query.order_by(cls.id.desc()).all()


class Post(db.Model):
    ''' The posts tablle'''

    __tablename__='posts'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    body=db.Column(db.Text(),nullable=False)
    date_added=db.Column(db.DateTime(),default=datetime.utcnow)
    user_id=db.Column(db.Integer(),db.ForeignKey('users.id'))
    comments=db.relationship('Comment',
        backref='post',lazy=True
    )

    def __init__(self,title,body):
        self.title=title
        self.body=body


    def __repr__(self):
        return f"< Post {self.title}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod 
    def get_all_desc(cls):
        return cls.query.order_by(cls.id.desc()).all()


class Comment(db.Model):
    ''' The comments table '''

    __tablename__='comments'
    id=db.Column(db.Integer(),primary_key=True)
    body=db.Column(db.Text(),nullable=False)
    date_added=db.Column(db.DateTime(),default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))

    def __init__(self,body):
        self.body=body


    def __repr__(self):
        return f"< Comment {self.id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod 
    def get_all_desc(cls):
        return cls.query.order_by(cls.id.desc()).all()