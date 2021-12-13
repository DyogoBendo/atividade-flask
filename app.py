from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager, current_user
from models import User, Notice

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

from routes.user_bp import user_bp
from routes.notice_bp import notice_bp

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(notice_bp, url_prefix='/notice')

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


@app.route('/')
def index():
    ESCRITORES = ["alana", "dyogo", "jefferson", "nikoly", "jimenez", "deivid"]
    try:
        username = current_user.username
        user = {"username": username, "writer": username in ESCRITORES, 'id': current_user.id}
    except:
        user = ''

    notices = Notice.query.all()
    object = {
        "user": user,
        "notices": notices
    }
    return render_template("index.html", object=object)    

@app.route("/login/")
def login():
    return render_template("login.html")

if __name__ == '__main__':    
    app.run(debub=True)
