from app import db
from datetime import datetime as dt

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # connect to the User table with its id

    def __repr__(self):
        return f'<Post: {self.body[:30]}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
