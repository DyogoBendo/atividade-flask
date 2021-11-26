import sys
from flask import render_template, redirect, url_for, request, abort
from models import Notice
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, current_user, logout_user
db = SQLAlchemy()
from datetime import date

def store():    
    if request.method == 'POST':

        form = request.form
        title = form['title']
        subtitle = form['subtitle']      
        text = form['text']      
        image = form['image']      
        idUser = form['idUser']      
        data = date.today()
        
        notice = Notice(title=title, subtitle=subtitle, text=text, image=image, id_user=idUser, date=data)

        db.session.add(notice)
        db.session.commit()    
        return redirect(url_for('user_bp.index'))
    else:
        render_template('create_notice')

def show(noticeId):
    notice = Notice.query.filter_by(id=noticeId).first()
    return render_template('show_notice.html', notice=notice)    
