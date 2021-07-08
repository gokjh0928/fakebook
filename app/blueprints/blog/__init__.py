from flask import Blueprint

# name, file(location reference), url_prefix
bp = Blueprint('blog', __name__, url_prefix='/blog')

from .import routes # AKA use routes from the same folder
