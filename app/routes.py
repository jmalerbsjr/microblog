from app import app

# A common pattern with decorators is to use them to register functions as callbacks for certain events
# These two decorators associate the URL's to it's function
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

