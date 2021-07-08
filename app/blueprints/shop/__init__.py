from flask import Blueprint

# name, file(location reference), url_prefix
bp = Blueprint('shop', __name__, url_prefix='/shop')

from .import routes # AKA use routes from the same folder
