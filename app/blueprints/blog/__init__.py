from flask import Blueprint

bp = Blueprint('blog', __name__, url_prefix='/blog')

<<<<<<< HEAD
from .import routes
=======
from .import routes, models
>>>>>>> d73017b5cc20016d4a5fb5cbe944b665f3696e16
