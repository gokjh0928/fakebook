<<<<<<< HEAD
from flask import jsonify, render_template, url_for
from .import bp as app
# current_app gets instance of currently running app
# jsonify converts python dict to json
=======
from .import bp as app
>>>>>>> 11cfe8ba5f502b36ad55db0f81c29ef2adf3c938

@app.route('/products')
def shop_products():
    pass

<<<<<<< HEAD

=======
>>>>>>> 11cfe8ba5f502b36ad55db0f81c29ef2adf3c938
@app.route('/cart')
def shop_cart():
    pass

<<<<<<< HEAD

=======
>>>>>>> 11cfe8ba5f502b36ad55db0f81c29ef2adf3c938
@app.route('/success')
def shop_success():
    pass

<<<<<<< HEAD

@app.route('/shop/failure')
def shop_failure():
    pass


@app.route('/shop/checkout')
def shop_checkout():
    pass
=======
@app.route('/failure')
def shop_failure():
    pass

@app.route('/checkout')
def shop_checkout():
    pass

>>>>>>> 11cfe8ba5f502b36ad55db0f81c29ef2adf3c938
