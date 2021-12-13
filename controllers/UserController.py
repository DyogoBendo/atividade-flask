import sys
from flask import render_template, redirect, url_for, request, abort
from flask.helpers import flash
from models import User
from flask_login import login_user, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
# from __main__ import db

db = SQLAlchemy()

def store():    
    form = request.form
    username = form['username']
    password = form['password']      

    user = User.query.filter_by(username=username).first()

    if user:
        if user.password == password:
            login_user(user, remember=False)
            return redirect(url_for('index'))
        else:            
            return redirect(url_for('login'))         
    user = User(username=username, password=password)

    db.session.add(user)
    db.session.commit()

    login_user(user, remember=False)
    return redirect(url_for('index'))

@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


def show(userId):
    pass


def update(userId):
    pass


def delete(userId):
    pass
