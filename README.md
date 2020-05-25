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
```bash
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
```
(they are now listed in the start.sh file)

# Launch

With an active virtual environment, run the file start.sh
```bash
sh start.sh
```
And click on the link terminal

# Status

In developments


