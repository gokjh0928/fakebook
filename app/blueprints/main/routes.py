# jsonify converts python dict to json
from flask import render_template
from .import bp as app
# current_app gets instance of currently running app

"""
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
"""

posts = [
    {
        'id': 1,
        'body': 'This is post 1',
        'author': 'Jay Kim',
        'timestamp': 'September 28'
    },
    {
        'id': 2,
        'body': 'This is post 2',
        'author': 'Jay Kim',
        'timestamp': 'September 10'
    },
    {
        'id': 3,
        'body': 'This is post 3',
        'author': 'Lucas Lang',
        'timestamp': 'September 4'
    }
]

# home page
@app.route('/')
@app.route('/home')
def home():
    context = {
        'posts': posts
    }
    return render_template('home.html', **context)

# contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# profile page
@app.route('/profile')
def profile():
    logged_in_user = 'Jay'
    return render_template("profile.html", u=logged_in_user)
