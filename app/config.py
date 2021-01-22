import os
from decouple import config

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY='a526a0bd09856cb5eaa229dc'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'app.db')
    SQLALCHEMY_ECHO=True
    DEBUG=True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'test.db')
    SQLALCHEMY_ECHO=True
    DEBUG=True
    TESTING=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=config('DATABASE_URI')
    SQLALCHEMY_ECHO=True
    DEBUG=False

