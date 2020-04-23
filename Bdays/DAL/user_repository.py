# TODO: Сделать абстрактный базовый класс для CRUD
import uuid

from Bdays.DAL.models.db import db
from Bdays.DAL.models.users import User 


class UserRepository():

    def create(self, id, username, password, role='user'):
        db_set = User(
            id = id,
            username = username,
            password = password,
            role = role
        )
        db.session.add(db_set)
        db.session.commit()
        return id


    def read(self, id):
        user = User.query.filter_by(id=id).first()
        return user


    def read_all(self):
        user = User.query.all()
        return user


    def update(self, id, username, password, role):
        user = User.query.filter_by(id=id).first()
        user.username = username
        user.password = password
        user.role = role
        db.session.commit()


    def find_user(self, username, password):
        user = User.query.filter(User.username == username).first()
        if user and user.check_password(password):
            return user
        

    def registration(self, username, password):
        id = uuid.uuid4()
        new_user = User(id=id ,username=username, role='user')
        new_user.set_password(password)
        user = User.query.filter(User.username == username).first()
        if not user:
            db.session.add(new_user)
            db.session.commit()
