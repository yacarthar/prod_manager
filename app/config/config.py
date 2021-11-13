"""
Module helper config
"""

import os

from dotenv import load_dotenv
from app.constants import ENV_FILE

load_dotenv(ENV_FILE)

class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ERROR_404_HELP=False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_TEST")
    # PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False


class LocalConfig(Config):
    SQLALCHEMY_ECHO = True
    DEBUG = True


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig,
    local=LocalConfig,
    test=TestingConfig
)
