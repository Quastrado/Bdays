from flask import Flask
from Bdays.DAL.models.db import db
from flask import Blueprint
from flask_login import LoginManager, current_user, login_required
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.controllers.login_controller import blueprint as login_blueprint
from Bdays.controllers.studio_members_controller import blueprint as studio_member_blueprint
from Bdays.controllers.index_controller import blueprint as index_blueprint
from Bdays.controllers.donations_controller import blueprint as donation_blueprint

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from config import BaseConfig


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
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', Server(host=app.config['HOST'], port=app.config['PORT']))
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = '/'
    

    engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url):
        create_database(engine.url)
    

    @login_manager.user_loader
    def load_user(id):
        return StudioMember.query.get(id)    

    with app.app_context():
        from Bdays.controllers import studio_members_controller, index_controller, login_controller
    
    return manager
