import logging

from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from db_operations import create_user, get_user
from forms import LoginForm, SignupForm
from users import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    log = current_app.logger
    form = LoginForm(request.form)
    if form.validate_on_submit():
        log.info('valid form')
        email = form.email.data
        password = form.password.data

        user = get_user(email)
        if not user or not check_password_hash(user.password, password):
            log.info('login failed')
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
        
        log.info('login success')
        login_user(user, remember=True)
        return redirect(url_for('profile'))
    return render_template('login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    log = current_app.logger
    # TODO implment form
    form = SignupForm(request.form)

    if form.validate_on_submit():
        # code to validate and add user to database goes here
        log.info('valid form')
        email = form.email.data
        name = form.name.data
        password = form.password.data

        user = get_user(email)
        if user:
            log.info('user with email %s found', user.email)

            # if a user is found, redirect to login page
            flash(f'Email {user.email} already exists')
            return redirect(url_for('auth.login'))
        
        new_user = User(email, name, generate_password_hash(password, method='sha256'), None, None)
        create_user(new_user)

        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('root'))
