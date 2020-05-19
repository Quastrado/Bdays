# Bdays

From time to time I communicate with some people. And each of them has a birthday once a year. I should keep that in mind! Maybe this application will help me a little ...

A more detailed description will come later

[HERE WILL BE A DESCRIPTION]


# Technologies

- Python 3.6.8
- Flask
- SQLAlchemy
- Bootstrap 4
- PostgreSQL 11.4


# Installation

First, you need to clone the repository using git

```bash
$ git clone https://github.com/Quastrado/Bdays
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
Create and add to the root of application folder file .env
Like this
```
SECRET_KEY = "2308fgby838v3r0871gf"
POSTGRES = '{'user':  'your username', 'password':  'your password', 'host':  'your host', 'database':  'your database name'}'

MAIL_SERVER = 'your smtp mail server'
MAIL_PORT = 'number of your port'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'your mail username'
MAIL_PASSWORD = 'your mail password'
```
And file .flaskenv
Like this
```
FLASK_APP = "Bdays"
FLASK_ENV = "development"
FLASK_DEBUG = "1"
```
Create tables in your database
```bash
$ python db upgrade
```

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


