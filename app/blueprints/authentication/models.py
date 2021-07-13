# make models through SQLAlchemy
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# the way to do it based solely on SQLAlchemy without using classes
followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200))
    bio = db.Column(db.Text)
    image = db.Column(db.String)    # reference to an image
    # backref will make it so that any Post object will display User info if ".address" is appended
    # lazy='dynamic' makes it so that posts will only be generated when used
    posts = db.relationship('Post', backref='author', lazy='dynamic')    
    followed = db.relationship(
        'User', 
        secondary = followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
        )

    def __repr__(self) -> str:
        return f'<User: {self.email}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    # hashes the password and does salting
    def create_password_hash(self, password):
        self.password = generate_password_hash(password)

    # checks the passed in password and sees if the password would equal one of the potential hashed passwords
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # create auxilary table(logged in user, person user chose to follow)
    def followed_posts(self):
        from app.blueprints.blog.models import Post
        # get posts for all users I'm following
        followed = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id)
        # get all of my own posts
        self_posts = Post.query.filter_by(user_id = self.id)
        # add them together and sort them using dates in descending order
        all_posts = followed.union(self_posts).order_by(Post.date_created.desc())
        return all_posts

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            db.session.commit()

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            db.session.commit()


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
