from . import db
from datetime import datetime


class Quotes:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,author,id,quote,permalink):
        
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = "http://quotes.stormconsultancy.co.uk/quotes/37" 


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
   

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    posts = db.relationship('Post', backref='user', lazy="dynamic")
   
    def __repr__(self):
        return f'Blog {self.username}'

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key = True)
    topic = db.Column(db.String(255))
    content = db.Column(db.String(255))
    posted_on = db.Column( db.DateTime, default=datetime.utcnow)
    profile_pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))
    comments = db.relationship('Comment', backref='user', lazy="dynamic")
   
    def __repr__(self):
        return f'Post {self.username}'

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
   
    def __repr__(self):
        return f'Comment {self.username}'
       