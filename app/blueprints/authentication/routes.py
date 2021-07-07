from .import bp as app
from flask import render_template, url_for, request, redirect
from .models import User
from flask_login import login_user, logout_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emailData = request.form.get('email')
        passwordData = request.form.get('password')

        # if email and password match what's in database
        user = User.query.filter_by(email=emailData).first()
        if user is None or not user.check_password(passwordData):
            return redirect(url_for('authentication.login'))
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('authentication/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication.login'))