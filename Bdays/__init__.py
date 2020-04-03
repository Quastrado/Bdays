from flask import Flask
from Bdays.models.db import db

from Bdays.models.studio_member import StudioMember
from datetime import datetime as dt


def create_app(test_config = False):
    app = Flask(__name__)
    if test_config:
        app.config.from_object('config.TestConfig')
    else:
        app.config.from_object('config.BaseConfig')
                
    db.init_app(app)

    with app.app_context():
        from Bdays import routes

    db.create_all(app=app)
    return app
