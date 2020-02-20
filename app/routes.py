from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def home():
    user = {'username': 'Sangamesh', 'occupation': 'student'}
    posts = [
    {
        'author' : {'username' : 'john'},
        'body' : 'Beatutiful day'
    },
    {
        'author' : {'username' : 'susan'},
        'body' : 'Beatutiful india'
    }
    ]

    return render_template('index.html', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
