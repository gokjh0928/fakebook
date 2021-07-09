# make models through SQLAlchemy
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200))

    def __repr__(self) -> str:
        return f'<User: {self.email}>'

    # hashes the password and does salting
    def create_password_hash(self, password):
        self.password = generate_password_hash(self.password)

    # checks the passed in password and sees if the password would equal one of the potential hashed passwords
    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)