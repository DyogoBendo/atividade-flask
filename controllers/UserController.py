import sys
from flask import render_template, redirect, url_for, request, abort
from flask.helpers import flash
from models import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def index():
    print(request)


def store():    
    form = request.form
    username = form['username']
    password = form['password']      

    exists_user = User.query.filter_by(username=username).first()

    if exists_user:
        if exists_user.password == password:
            return redirect(url_for('index'))
        else:            
            return redirect(url_for('login'))
        
    user = User(username=username, password=password)

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('index'))


def show(userId):
    pass


def update(userId):
    pass


def delete(userId):
    pass
