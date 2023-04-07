from flask import Flask
from config import Config
from .database import db
from os import path
from .routes.gpt_routes import gpt_routes
from .routes.home_routes import home_routes
from .routes.auth_routes import auth_routes
from flask_login import LoginManager
from .models.user import User
from flask_migrate import Migrate



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(home_routes, url_prefix='/')
    app.register_blueprint(gpt_routes, url_prefix='/')
    app.register_blueprint(auth_routes, url_prefix='/')
    db.init_app(app)
    migrate = Migrate(app, db)# allow to migrate changes in the database when develop

    create_database(app)

    login_manager = LoginManager()#This object is used to hold the settings used for logging in.
    login_manager.init_app(app)
    #customize for redirect to login page if login_required failed
    login_manager.login_view = 'auth_routes.login'
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    DB_NAME = "database.db"
    #create the database structure if we dont have one
    if not path.exists('flask_app/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')