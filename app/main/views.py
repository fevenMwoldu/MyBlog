from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quotes


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
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    return render_template('index.html',quotes=quotes)

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

    # Retrieve articles for source_id
    quotes = get_quotes(quote_id)

    return render_template('quotes.html', quotes=quotes)
