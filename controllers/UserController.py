import sys
from flask import render_template, redirect, url_for, request, abort
from flask.helpers import flash
from models import User
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, current_user
db = SQLAlchemy()


@login_required
def index():
    return render_template('index.html', username=current_user.username)


def store():    
    form = request.form
    username = form['username']
    password = form['password']      

    user = User.query.filter_by(username=username).first()

    if user:
        if user.password == password:
            login_user(user, remember=False)
            return redirect(url_for('user_bp.index'))
        else:            
            return redirect(url_for('login'))         
    user = User(username=username, password=password)

    db.session.add(user)
    db.session.commit()

    login_user(user, remember=False)
    return redirect(url_for('user_bp.index'))


def show(userId):
    pass


def update(userId):
    pass


def delete(userId):
    pass
