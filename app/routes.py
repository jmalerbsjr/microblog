from flask import render_template
from app import app

# A common pattern with decorators is to use them to register functions as callbacks for certain events
# These two decorators associate the URL's to it's function
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joseph'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home',user=user,posts=posts)