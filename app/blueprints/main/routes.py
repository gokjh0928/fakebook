# jsonify converts python dict to json
from flask import render_template, request, redirect, url_for, flash
from .import bp as app
from flask_login import current_user, login_required
from app import db
from app.blueprints.authentication.models import User
from app.blueprints.blog.models import Post
import boto3
from flask import current_app
import time

"""
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
"""

# home page
@app.route('/', methods=['GET', 'POST'])
@login_required
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
@login_required
def profile():
    s3 = boto3.client('s3', aws_access_key_id=current_app.config.get(
        'AWS_ACCESS_KEY_ID'), aws_secret_access_key=current_app.config.get('AWS_SECRET_ACCESS_KEY'))
    print(s3)
    
    if request.method == 'POST':  
        u = User.query.get(current_user.id)
        u.first_name = request.form.get('first-name')
        u.last_name = request.form.get('last-name')
        u.email = request.form.get('email')
        u.bio = request.form.get('bio')
        if len(request.files) > 0:
            s3.upload_fileobj(
                # get the object
                request.files.get('profile-image'),
                # bucket name
                'jay-fakebook',
                # name of file
                request.files.get('profile-image').filename,
                ExtraArgs={
                    'ACL': 'public-read',
                    'ContentType': request.files.get('profile-image').content_type
                }
            )
            u.image = f"{current_app.config.get('AWS_BUCKET_LOCATION')}{request.files.get('profile-image').filename}"
        db.session.commit()
        flash('Profile updated sucessfully', 'info')
        return redirect(url_for('main.profile'))

    context = {
        'posts': current_user.followed_posts() if current_user.is_authenticated else []
    }
    return render_template("profile.html", **context)
