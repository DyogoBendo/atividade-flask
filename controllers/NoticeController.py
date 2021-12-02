import sys
from flask import render_template, redirect, url_for, request, abort
from models import Notice, User
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, current_user, logout_user
db = SQLAlchemy()
from datetime import date
ESCRITORES = ["alana", "dyogo", "jefferson", "nikoly", "jimenez", "deivid"]

@login_required
def store():    
    if request.method == 'POST':

        form = request.form
        title = form['title']
        subtitle = form['subtitle']      
        text = form['text']      
        image = form['image']      
        idUser = User.query.filter_by(username=current_user.username).first().id
        data = date.today()
        
        notice = Notice(title=title, subtitle=subtitle, text=text, image=image, id_user=idUser, date=data)

        db.session.add(notice)
        db.session.commit()    
        return redirect(url_for('index'))
    else:                
        username = current_user.username
        user = {"username": username, "writer": username in ESCRITORES}
        return render_template('create_notice.html', user = user)

def show(notice_id):    
    notice = Notice.query.filter_by(id=notice_id).first()    
    author = User.query.filter_by(id=notice.id_user).first()
    try:
        username = current_user.username
        user = {"username": username, "writer": username in ESCRITORES}
    except:
        user = ''

    object = {
        "user": user,
        "notice": notice,
        "author": author
    }

    return render_template('show_notice.html', object=object)    
