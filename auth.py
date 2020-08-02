import logging

from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from db_operations import create_user, get_user
from forms import LoginForm, SignupForm
from users import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    log = current_app.logger

    if current_user.is_authenticated:
        return redirect(url_for('root'))

    form = LoginForm()
    signupform = SignupForm()
    if form.validate_on_submit():
        log.info('valid form')
        email = form.email.data
        password = form.password.data

        user = get_user(email)
        if not user or not check_password_hash(user.password, password):
            log.info('login failed')
            flash('Please check your login details and try again.')
            return redirect(url_for('root'))
        
        log.info('login success')
        login_user(user, remember=True)
        return redirect(url_for('root'))
    return render_template('login.html', loginform=form, signupform=signupform)

@auth.route('/test', methods=['GET'])
def test():
    return ok

@auth.route('/signup', methods=['POST'])
def signup():
    log = current_app.logger

    if current_user.is_authenticated:
        return redirect(url_for('root'))
    
    form = SignupForm(request.form)
    if form.validate_on_submit():
        # add user to database
        log.info('valid signup form')
        email = form.email.data
        name = form.name.data
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        
        new_user = User(email, name, hashed_password, None, None)
        create_user(new_user)

        return redirect(url_for('root'))

    return render_template('signup.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('root'))
