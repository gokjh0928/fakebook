from .import bp as app
from app import db
from flask import render_template, url_for, request, redirect, flash     # request is to send a request to server
from .models import User
from flask_login import login_user, logout_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emailData = request.form.get('email')
        passwordData = request.form.get('password')
        # check if email and password match what's in the database
        user = User.query.filter_by(email=emailData).first()
        # see if a user exists for this unique email and the password matches the input password
        if user is None or not user.check_password(passwordData):
            return redirect(url_for('authentication.login'))
        login_user(user)
        flash('User logged in successfully', 'success')
        return redirect(url_for('main.home'))
    return render_template('authentication/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =='POST':
        # check if the email used for registration is already in the database
        user = User.query.filter_by(email = request.form.get('email')).first()
        # if user already exists
        if user is not None:
            # send a message to inform this and redirect back to the register
            flash('A user associated with this email already exists. Try again.', 'danger')
            return redirect(url_for('authentication.register'))
        # if the password and the confirm_password fields aren't the same value
        if request.form.get('password') != request.form.get('confirm_password'):
            # send a message to inform this and redirect back to the register
            flash(
                'Your passwords don\'t match. Try again.', 'danger')
            return redirect(url_for('authentication.register'))

        # now can get on with registering the new User, grab form data
        u = User(
            first_name = request.form.get('first_name'),
            last_name = request.form.get('last_name'),
            email = request.form.get('email')
        )
        u.create_password_hash(request.form.get('password'))
        u.save()
        flash('User registered successfully', 'success')
        return redirect(url_for('authentication.login'))
    return render_template('authentication/register.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('User logged out successfully', 'warning')
    return redirect(url_for('main.home'))
