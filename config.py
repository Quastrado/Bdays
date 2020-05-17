import ast
import os
from datetime import timedelta

class BaseConfig:
	SECRET_KEY = os.getenv('SECRET_KEY')
	DEBUG = True
	REMEMBER_COOKIE_DURATION = timedelta(days=3)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	POSTGRES = eval(os.getenv('POSTGRES'))
	SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(password)s@%(host)s/%(database)s' % POSTGRES
		
	MAIL_SERVER = os.getenv('MAIL_SERVER')
	MAIL_PORT = os.getenv('MAIL_PORT')
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.getenv('MAIL_USERNAME')
	MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

class TestConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')