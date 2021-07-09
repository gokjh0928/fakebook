from app import create_app, db
from app.blueprints.authentication.models import User
# the above db and User imports provides a shortcut for when running flask shell in terminal

app = create_app()

@app.shell_context_processor
def make_context():
    return {
        'db': db,
        'User': User
    }
