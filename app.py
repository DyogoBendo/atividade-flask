from flask import Flask, render_template
from flask_migrate import Migrate
from models import db
from routes.user_bp import user_bp
from config import Config
from flask_login import LoginManager
from models import User
from routes.notice_bp import notice_bp

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(notice_bp, url_prefix='/notice')

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template("index.html")    

@app.route("/login/")
def login():
    return render_template("login.html")



if __name__ == '__main__':    
    app.run(debub=True)
