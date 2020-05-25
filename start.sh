#!/usr/bin/env bash

export FLASK_APP="Bdays"
export FLASK_ENV="development"
export FLASK_DEBUG="1"
export HOST="your host"
export PORT="your port"

export SECRET_KEY="your secret key"
export DATABASE_URI="postgresql://postgres:postgres@127.0.0.1/your_db_name"
export MAIL_SERVER='your smtp server'
export MAIL_PORT= 'your mail port'
export MAIL_USE_TLS=False
export MAIL_USE_SSL=True
export MAIL_USERNAME='your mail username'
export MAIL_PASSWORD='your mail password'
python main.py db upgrade
python main.py runserver

