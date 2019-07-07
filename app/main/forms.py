from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired
from ..models import User, Blog, Post, Comment, Subscription
from datetime import datetime


class PostForm(FlaskForm):
    topic = StringField('Enter the topic of your post',validators=[DataRequired()])
    post_content = TextAreaField('Your New postcontent here',validators=[DataRequired()])
    submit = SubmitField()

class CommentForm(FlaskForm):
    comment = TextAreaField('Insert your comment here', validators=[DataRequired()])
    submit = SubmitField()

class SubscriptionForm(FlaskForm):
    email = StringField('Insert your email here', validators=[DataRequired()])
    submit = SubmitField()

