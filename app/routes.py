from app import app
from flask import jsonify, render_template

"""
CREATE - POST
READ   - GET
UPDATE - PUT
DELETE - DELETE
"""

@app.route('/users')
def get_users():
    return jsonify({ 'message': 'This works!' })

# profile
@app.route('/profile')
def profile():
    logged_in_user = 'Derek'
    return render_template('profile.html', u=logged_in_user)

# blog
@app.route('/blog')
def blog():
    return "This is the blog page."

# contact
@app.route('/contact')
def contact():
    return "This is the contact page."