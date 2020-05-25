# Bdays

A simple web application designed to create, store, modify and provide birthday information for a given circle of people

# Technologies

- Python 3.6.8
- Flask
- SQLAlchemy
- Bootstrap 4
- PostgreSQL 11.4


# Installation

First, you need to clone the repository using git

```bash
$ git clone --single-branch --branch fix/#2_startup_fix https://github.com/Quastrado/Bdays
```
Then create a virtual environment in the project folder using the venv tool
```bash
$ python3 -m venv env
```
And activate the virtual environment
```bash
$ . env/bin/activate
```
Using file requirements.txt, install neсessary modules and packages
```bash
$ pip install -r requirements.txt
```
You will need the following environment variables:
```
FLASK_APP = "Bdays"
FLASK_ENV = "development"
FLASK_DEBUG = "1"

SECRET_KEY = "your secret key"
POSTGRES = '{'user':  'your username', 'password':  'your password', 'host':  'your host', 'database':  'your database name'}'
MAIL_SERVER = 'your smtp mail server'
MAIL_PORT = 'number of your port'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'your mail username'
MAIL_PASSWORD = 'your mail password'
```
(they are now listed in the start.sh file)

# Launch

Open the terminal in the application folder and activate virtual enviroment
```bash
$ . env/bin/activate
```
Launch the application
```bash
$ flask run
```
And click on the link terminal

# Status

In developments


