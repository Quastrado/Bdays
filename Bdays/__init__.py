from flask import Flask
from Bdays.DAL.models.db import db
from flask import Blueprint
from Bdays.controllers.login_controller import blueprint as login_blueprint
from Bdays.controllers.studio_members_controller import blueprint as studio_member_blueprint
from Bdays.controllers.index_controller import blueprint as index_blueprint
from Bdays.controllers.donations_controller import blueprint as donation_blueprint


def create_app(test_config = False):
    app = Flask(__name__)
    app.register_blueprint(login_blueprint, url_prefix='/login')
    app.register_blueprint(studio_member_blueprint, url_prefix='/studio_member')
    app.register_blueprint(index_blueprint, url_prefix='/')
    app.register_blueprint(donation_blueprint, url_prefix='/donation')
    if test_config:
        app.config.from_object('config.TestConfig')
    else:
        app.config.from_object('config.BaseConfig')
                
    db.init_app(app)
    

    with app.app_context():
        from Bdays.controllers import studio_members_controller, index_controller

    db.create_all(app=app)
    return app
