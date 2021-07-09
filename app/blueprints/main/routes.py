# jsonify converts python dict to json
from flask import render_template, request, redirect, url_for, flash
from .import bp as app
from flask_login import current_user
from app import db
from app.blueprints.authentication.models import User
from app.blueprints.blog.models import Post
# current_app gets instance of currently running app

"""
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
"""

# home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if current_user.is_authenticated:
            u = User.query.get(current_user.id)
            body_text = request.form.get('body_text')
            post = Post(user_id = current_user.id, body = body_text)
            post.save()
            flash('Blog post was sucessfully posted', 'success')
        else:
            flash('You can only post once logged in!', 'danger')
        return redirect(url_for('main.home'))
    context = {
        'posts': current_user.followed_posts() if current_user.is_authenticated else []
    }
    return render_template('home.html', **context)

# contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# profile page
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        #print(request.files.get('profile_image'))
        u = User.query.get(current_user.id)
        u.first_name = request.form.get('first-name')
        u.last_name = request.form.get('last-name')
        u.email = request.form.get('email')
        db.session.commit()
        flash('Profile updated sucessfully', 'info')
        return redirect(url_for('main.profile'))
    context = {
        'posts': current_user.followed_posts() if current_user.is_authenticated else []
    }
    return render_template("profile.html", **context)
