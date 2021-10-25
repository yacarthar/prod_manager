"""
Module create flask application
"""

import logging

from flask import Flask
from flask_migrate import Migrate

from app.config import app_config
from app.api.model import db
from app.api import api_v1_blueprint

from app.core.errors import AppBaseException, handle_app_error


def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.DEBUG)
    app.app_context().push()
    with app.app_context():
        app.config.from_object(app_config)

        db.init_app(app)
        migrate = Migrate(app, db)
        
        app.register_blueprint(api_v1_blueprint)
        app.register_error_handler(AppBaseException, handle_app_error)

        db.create_all()  # TBD: check table exists

    return app


