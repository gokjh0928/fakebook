from .import bp as app
from flask import render_template, request, url_for, flash, redirect
from flask_login import current_user
from app import db
from app.blueprints.authentication.models import User

posts = [
        {
            'id': 1,
            'body': 'This is the first blog post',
            'author': 'Lucas L.',
            'timestamp': '10-2-2020',
            'items': {
                'health': 10,
                'mana': 5
            }
        },
        {
            'id': 2,
            'body': 'This is the second blog post',
            'author': 'Derek H.',
            'timestamp': '10-25-2020',
            'items': {
                'health': 8,
                'mana': 3
            }
        },
        {
            'id': 3,
            'body': 'This is the third blog post',
            'author': 'Joel Carter',
            'timestamp': '11-2-2020',
            'items': {
                'health': 9,
                'mana': 9
            }
        }
    ]

@app.route('/')
def home():
    context = {
        'posts': posts
    }
    return render_template('home.html', **context)

# profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        u = User.query.get(current_user.id)
        u.first_name = request.form.get('first_name')
        u.last_name = request.form.get('last_name')
        u.email = request.form.get('email')
        db.session.commit()
        flash('Profile updated successfully', 'info')
        return redirect(url_for('main.profile'))
    return render_template('profile.html')

# contact
@app.route('/contact')
def contact():
    return "This is the contact page."