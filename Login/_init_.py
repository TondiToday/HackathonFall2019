from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bd = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config[''] =
    app.config[''] =

    db.init_app(app)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    