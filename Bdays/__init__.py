from flask import Flask
from Bdays.models.db import db
from Bdays.controllers.studio_members_controller import blueprint as studio_member_blueprint
from Bdays.controllers.base_controller import blueprint as base_blueprint
#from Bdays.models.studio_member import StudioMember



def create_app(test_config = False):
    app = Flask(__name__)
    app.register_blueprint(studio_member_blueprint, url_prefix='/studio_member')
    app.register_blueprint(base_blueprint, url_prefix='/')
    if test_config:
        app.config.from_object('config.TestConfig')
    else:
        app.config.from_object('config.BaseConfig')
                
    db.init_app(app)

    with app.app_context():
        from Bdays.controllers import studio_members_controller, base_controller

    db.create_all(app=app)
    return app
