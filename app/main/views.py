from flask import render_template
from . import main

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
    return render_template('index.html')

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
