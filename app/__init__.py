from flask import Flask

# Flask uses the location of the module passed here as a starting point when it needs to load associated resources
app = Flask(__name__)

# The bottom import is a workaround to circular imports, a common problem with Flask applications
from app import routes

