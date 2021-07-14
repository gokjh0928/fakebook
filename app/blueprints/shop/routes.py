from time import strptime
from flask.helpers import url_for
from .import bp as app
from flask import json, render_template, redirect, flash, request, session, current_app, jsonify
from .models import Product, Cart, StripeProduct
from flask_login import current_user
import stripe
from app import db
import pprint

@app.route('/')
def index():
    """
    [GET] /shop
    """
    stripe.api_key = current_app.config.get('STRIPE_SECRET_KEY')
    # print(stripe.Product.list())
    # print(stripe.Price.retrieve('price_1JCnOKInbeNyBE8aEngKCetu'))
    context = {
        'products': StripeProduct.query.all()
    }
    print(StripeProduct.query.all())
    return render_template('shop/index.html', **context)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    """
    [GET] /shop/cart
    """
    from app.context_processors import build_cart
    display_cart = build_cart()['cart_dict']
    session['session_display_cart'] = display_cart
    if request.method == 'POST':
        # Clear the current user's cart to make way for the new objects
        display_cart = build_cart()['cart_dict']
        session['session_display_cart'] = display_cart
        [db.session.delete(i) for i in Cart.query.filter_by(user_id=current_user.id).all()]
        # reset the sequence for the cart IDs for the newly added cart objects
        db.session.execute('ALTER SEQUENCE cart_id_seq RESTART WITH 1;')
        db.session.commit()
        for idx, new_amount in enumerate(request.form.getlist('amount')):
            curr_obj_id = list(display_cart.values())[idx]['product_id']
            # get the matching object and create copies to add to the cart
            for _ in range(int(new_amount)):
                Cart(user_id=current_user.id, product=curr_obj_id).save()
        flash('Updated quantities', 'info')
        return redirect(url_for('shop.cart'))
    context = {
        'cart': display_cart.values()
    }
    #pprint.pprint(display_cart.values())

    if not current_user.is_authenticated:
        flash('You must login to view your cart', 'warning')
        return redirect(url_for('authentication.login'))
    return render_template('shop/cart.html', **context)

@app.route('/cart/add')
def add_to_cart():
    """
    [GET] /shop/cart/add
    """
    if not current_user.is_authenticated:
        flash('You must login to add items to your cart', 'warning')
        return redirect(url_for('authentication.login'))

    # Make a new product
    product = StripeProduct.query.get(request.args.get('id'))

    # Save it to their cart
    Cart(user_id=current_user.id, product=product.stripe_product_id).save()
    flash(f'You have added {product.name} to the cart', 'success')
    return redirect(url_for('shop.index'))

@app.route('/cart/remove')
def remove_from_cart():
    if not current_user.is_authenticated:
        flash('You must login to remove items from your cart', 'warning')
        return redirect(url_for('authentication.login'))
    [db.session.delete(i) for i in Cart.query.filter_by(product=request.args.get('product_id')).all()]
    db.session.commit()
    product_name = StripeProduct.query.filter_by(stripe_product_id=request.args.get('product_id')).first().name
    flash(f'Removed {product_name}', 'info')
    return redirect(url_for('shop.cart'))

@app.route('/success')
def shop_success():
    pass

@app.route('/failure')
def shop_failure():
    pass

@app.route('/checkout', methods=['POST'])
def checkout():
    stripe.api_key = current_app.config.get('STRIPE_SECRET_KEY')
    dc = session.get('session_display_cart')
    
    l_items = []
    for product in dc.values():
        product_dict = {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product['name'],
                        'images': [product['image']]
                    },
                    'unit_amount': int(float(product['price']) * 100),
                },
                'quantity': product['quantity'],
            }
        l_items.append(product_dict)

    try:
        # Handle payment
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=l_items,
            mode='payment',
            success_url='http://localhost:5000/shop/cart',
            cancel_url='http://localhost:5000/shop/cart',
        )

        # Clear all items from cart
        [db.session.delete(i) for i in Cart.query.filter_by(user_id=current_user.id).all()]
        db.session.commit()

        flash('Your order was processed successfully', 'primary')
        return jsonify({ 'session_id': checkout_session.id })
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/seed')
def seed_stripe_products():
    stripe.api_key = current_app.config.get('STRIPE_SECRET_KEY')

    def seed_data():
        # print(stripe.Product.list().get('data'))
        list_to_store_in_db = []

        # Clear all items from database
        [db.session.delete(i) for i in StripeProduct.query.all()]
        db.session.commit()

        for p in stripe.Product.list().get('data'):
            list_to_store_in_db.append(StripeProduct(stripe_product_id=p['id'], name=p['name'], image=p['images'][0], description=p['description'], price=int(float(p['metadata']['price']) * 100), tax=int(float(p['metadata']['tax']) * 100)))
        
        db.session.add_all(list_to_store_in_db)
        db.session.commit()

    seed_data()
    return jsonify({ 'message': 'Success' })