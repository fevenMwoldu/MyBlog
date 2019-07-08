from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quotes
from flask_login import login_required
from ..models import User, Blog, Post, Comment, Subscription
from .. import db,photos
from .forms import PostForm,CommentForm,SubscriptionForm
from ..email import mail_message


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20,2018'
    },
    {
        'author': 'Jhon Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21,2018'
    }

]

# Views
@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''

    form = SubscriptionForm()

    if form.validate_on_submit():        
        new_subscription = Subscription(email=form.email.data)
        new_subscription.save_email()

    quotes = get_quotes()
    
    posts = Post.query.order_by(Post.posted_on.desc()).all()

    return render_template('index.html', SubscriptionForm = form, quotes=quotes, posts=posts)

@main.route('/home')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('home.html', posts=posts)

@main.route('/about')
def about():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('about.html',title='About')

@main.route('/quotes/<string:quote_id>')
def quotes(quote_id):
    '''
    View Newse page function that returns the News details page and its data
    '''

    # Retrieve articles for quote_id
    quotes = get_quotes(quote_id)

    return render_template('quotes.html', quotes=quotes)


@main.route('/Addpost', methods=["GET", "POST"])
def Addpost():
    form = PostForm()
    
    if form.validate_on_submit():
        new_post = Post(content=form.post_content.data, topic=form.topic.data)
        new_post.save_post()

        # send emails to all blog subscribers
        subs = Subscription.query.all()
        for sub in subs:
            mail_message("New Post Added","email/post_notification", sub.email, post=new_post)

        return redirect(url_for('.index'))
    title = 'Adding new posts'
    return render_template('AddPost.html', PostForm=form, title=title)

@main.route('/Addcomment', methods=["GET", "POST"])
def Addcomment():
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data)
        new_comment.save_comment()
        return redirect(url_for('.index'))
    title = 'Adding comments'
    return render_template('comment.html', CommentForm=form, title=title)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(fullname = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def post(id):
    form = CommentForm()

    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data, post_id=id)
        new_comment.save_comment()


    post = Post.query.filter_by(id=id).first()
    
    if post is not None:
        return render_template('post.html', CommentForm=form, post=post)

    return redirect(url_for('.index'))

