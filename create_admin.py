from getpass import getpass
import sys
import uuid

from Bdays import create_app
from Bdays.DAL.models.db import db
from Bdays.DAL.models.users import User


app = create_app()


with app.app_context():
    username = input('Enter name: ')

    if User.query.filter(User.username == username).count():
        print('Such user already exists')
        sys.exit(0)

    password = getpass('Enter password: ')
    password_repeat = getpass('Repeat password: ')

    if not password == password_repeat:
        print('Passwords do not match')
        sys.exit(0)

    uid = uuid.uuid4()

    new_user = User(id = uid, username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print(f'User with id {uid} added')