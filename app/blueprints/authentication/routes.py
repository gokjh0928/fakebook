from .import bp as app
from flask import render_template, url_for, request, redirect     # request is to send a request to server
from .models import User
from flask_login import login_user, logout_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emailData = request.form.get('email')
        passwordData = request.form.get('password')
        # check if email and password match what's in the database
        user = User.query.filter_by(email=emailData).first()
        # see if a user exists for this unique email and the passwrod matches the input password
        if user is None or not user.check_password(passwordData):
            return redirect(url_for('authentication.login'))
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('authentication/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
