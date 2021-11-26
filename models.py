from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User (UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,            
            'password': self.password
        }


class Notice (db.Model):
    __tablename__ = 'notice'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.Text)
    subtitle = db.Column(db.Text)
    text = db.Column(db.Text)
    date = db.Column(db.Date)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,            
            'image': self.image,
            'subtitle': self.subtitle,
            'text': self.text,
            'date': self.date,
            'id_user': self.id_user
        }

class Commentary (db.Model):
    __tablename__ = 'commentary'
    id = db.Column(db.Integer, primary_key=True)    
    content = db.Column(db.Text)    
    date = db.Column(db.Date)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"))
    id_notice = db.Column(db.Integer, db.ForeignKey("user.id"))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'content': self.title,                        
            'date': self.date,
            'id_user': self.id_user,
            'id_notice': self.id_notice
        }