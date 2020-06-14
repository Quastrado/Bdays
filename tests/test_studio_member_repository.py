import datetime
import pytest
import uuid

from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from tests.test_base import app
from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.DAL.models.roles import Role
from Bdays.DAL.studio_member_repository import StudioMemberRepository

repository = StudioMemberRepository()


"""create method tests"""
def test_studio_member_create_successfull(client):
    new_user = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    assert StudioMember.query.filter_by(nickname='user').first()
    repository.delete(new_user)


def test_return_id(client):
    user_id = repository.create('email@dot.com', 'user1', '01.01.2000', 'Studio Member') 
    assert user_id
    repository.delete(user_id)

def test_missing_nickname(client):
    with pytest.raises(TypeError):
        repository.create('email@dot.com', '01.01.2000', 'Studio Member')


def test_not_unique_nickname(client):
    user = repository.create('email@dot.com', 'user2', '01.01.2000', 'Studio Member')
    with pytest.raises(IntegrityError):
        user_with_same_name = repository.create('email@dot.com', 'user2', '01.01.2000', 'Studio Member')
    db.session.rollback()
    repository.delete(user)


def test_role_assignment(client):
    user_id = repository.create('email@dot.com', 'user3', '01.01.2000', 'Studio Member')
    user = repository.read(user_id)
    assert db.session.query(Role).filter(Role.role == 'Studio Member').first() in user.role
    repository.delete(user_id)


def test_invalid_email(client):
    with pytest.raises(ValueError):
        new_user = repository.create('emaildotcom', 'user4', '01.01.2000', 'Studio Member')


""" read method tests"""
def test_read_successfull(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    assert repository.read(user_id)
    repository.delete(user_id)


def test_create_missing_id(client):
    with pytest.raises(TypeError):
        user = repository.read()

""" read all method tests"""
def test_read_all_successfull(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    user = repository.read(user_id)
    all_users = repository.read_all()
    assert user in all_users
    repository.delete(user_id)


"""update method tests"""
def test_update_successfull(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    updated_user = repository.update(user_id, 'updated_user', '02.02.2002')
    updated_user = repository.read(user_id)
    assert updated_user.nickname == 'updated_user' and updated_user.birthday == datetime.date(2002, 2, 2)
    repository.delete(user_id)


def test_update_missing_id(client):
    with pytest.raises(TypeError):
        updated_user = repository.update('updated_user', '02.02.2002')


def test_update_missing_argument(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    with pytest.raises(TypeError):
        updated_user = repository.update(user_id, 'updated_user')
    db.session.rollback()
    repository.delete(user_id)


"""delete method test"""
def test_delete_successfull(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    repository.delete(user_id)
    assert repository.read(user_id) == None


def test_delete_missing_id(client):
    with pytest.raises(TypeError):
        repository.delete()


"""find studio member method test""" 
def test_find_studio_member(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    password = 'password'
    repository.set_password(user_id, password)
    assert repository.find_studio_member('user', password)
    repository.delete(user_id)


def test_incorrect_password(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    password = 'password'
    incorrect_password = 'passw0rd'
    repository.set_password(user_id, password)
    assert repository.find_studio_member('user', incorrect_password) == None
    repository.delete(user_id)


def test_nonexistent_user(client):
    assert repository.find_studio_member('user', 'password') == None


def test_missing_argument(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    password = 'password'
    repository.set_password(user_id, password)
    with pytest.raises(TypeError):
        repository.find_studio_member('user')
    db.session.rollback()
    repository.delete(user_id)


"""set password method test"""
def test_set_password(client):
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    model = StudioMember()
    password = 'password'
    repository.set_password(user_id, password)
    user = repository.read(user_id)
    assert user.password and check_password_hash(user.password, password)
    repository.delete(user_id)


def test_missing_id(client):
    password = 'password'
    with pytest.raises(TypeError):
        repository.set_password(password)