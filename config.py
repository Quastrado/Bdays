import ast
import os
from datetime import timedelta


class BaseConfig:
	SECRET_KEY = "your secret key"
	DEBUG = True
	HOST = "your host"
	PORT = "your port"
	REMEMBER_COOKIE_DURATION = timedelta(days=3)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = "your database uri"
	MAIL_SERVER = "your mail server"
	MAIL_PORT = "your mail port"
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = "your mail username"
	MAIL_PASSWORD = "your mail password"

class TestConfig:
    SECRET_KEY = "your secret key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "your database uri"

