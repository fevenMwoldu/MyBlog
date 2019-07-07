from . import db
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quotes:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,author,id,quote,permalink):
        
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = "http://quotes.stormconsultancy.co.uk/quotes/37" 


class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_secure = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
   

    def __repr__(self):
        return f'User {self.fullname}'

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    posts = db.relationship('Post', backref='user', lazy="dynamic")
   
    def __repr__(self):
        return f'Blog {self.title}'

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

    def save_post(self):
        db.session.add(self)
        db.session.commit()
   
    def __repr__(self):
        return f'Post {self.topic}'

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
   
    def __repr__(self):
        return f'Comment {self.comment}'

class Subscription(db.Model):
    __tablename__ = 'subscription'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255))

    def save_email(self):
        db.session.add(self)
        db.session.commit()
   
    def __repr__(self):
        return f'Subscription {self.email}'
       