import os

class Config:
    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret'
    FLASK_APP = os.environ.get('FLASK_APP') or 'app.py'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    DB_NAME = os.environ.get('DB_NAME') or "database.db"

    # Database Config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False