from flask import jsonify, render_template, url_for
from .import bp as app
# current_app gets instance of currently running app
# jsonify converts python dict to json

@app.route('/products')
def shop_products():
    pass


@app.route('/cart')
def shop_cart():
    pass


@app.route('/success')
def shop_success():
    pass


@app.route('/shop/failure')
def shop_failure():
    pass


@app.route('/shop/checkout')
def shop_checkout():
    pass
