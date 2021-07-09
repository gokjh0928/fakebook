from flask import Blueprint

# name, file(location reference), url_prefix
bp = Blueprint('blog', __name__, url_prefix='/blog')

from .import routes, models # AKA use routes and models from the same folder
