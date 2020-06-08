#!/usr/bin/env bash

export FLASK_APP="Bdays"
export FLASK_ENV="development"
export FLASK_DEBUG="1"
export HOST="0.0.0.0"
export PORT="5000"

export SECRET_KEY="your secret key"
export DATABASE_URI="postgresql://bdays:sfa@127.0.0.1/bdays"
export MAIL_SERVER='smtp.yandex.com'
export MAIL_PORT=465
export MAIL_USE_TLS=False
export MAIL_USE_SSL=True
export MAIL_USERNAME='EthexEnterprise@yandex.ru'
export MAIL_PASSWORD='sfabdays'
python main.py db upgrade
pytest
python main.py runserver
