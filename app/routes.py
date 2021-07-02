from app import app
from flask import jsonify, render_template   # jsonify converts python dict to json

"""
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
"""
# listen in for a new route
@app.route('/users')
def get_users():
    return jsonify({'message': 'This works!'})

# listen in for a new route
@app.route('/profile')
def get_profile():
    logged_in_user = 'Jay'
    return render_template("profile.html", u=logged_in_user)


# listen in for a new route
@app.route('/blog')
def get_blog():
    return render_template("blog.html")

# listen in for a new route
@app.route('/contact')
def get_contact():
    return render_template("contact.html")
