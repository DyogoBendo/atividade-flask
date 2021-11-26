from flask import Flask, render_template
from flask_migrate import Migrate
from models import db
from routes.user_bp import user_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix='/users')


@app.route('/')
def index():
    return render_template("index.html")    

@app.route("/login/")
def login():
    return render_template("login.html")



if __name__ == '__main__':    
    app.run(debub=True)
