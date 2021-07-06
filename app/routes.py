from flask import jsonify, render_template, current_app as app
from app.blueprints.blog.routes import posts

"""
CREATE - POST
READ   - GET
UPDATE - PUT
DELETE - DELETE
"""

@app.route('/')
def home():
    context = {
        'posts': posts
    }
    return render_template('home.html', **context)

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

@app.route('/shop/products')
def shop_products():
    pass

@app.route('/shop/cart')
def shop_cart():
    pass

@app.route('/shop/success')
def shop_success():
    pass

@app.route('/shop/failure')
def shop_failure():
    pass

@app.route('/shop/checkout')
def shop_checkout():
    pass


