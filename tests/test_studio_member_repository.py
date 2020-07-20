import datetime
import pytest
import uuid

from sqlalchemy.exc import DataError, IntegrityError
from werkzeug.security import check_password_hash

from tests.test_base import app
from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.DAL.models.roles import Role
from Bdays.DAL.studio_member_repository import StudioMemberRepository
from Bdays.DAL.DTO.studio_member import StudioMember as StudioMemberDTO


"""create method tests"""
def test_studio_member_create_successfull(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'email@dot.com'
    dto.nickname = 'user'
    dto.birthday = '01.01.2000'
    new_user = repository.create(dto, 'Studio Member')
    assert StudioMember.query.filter_by(nickname='user').first()
    repository.delete(new_user)


def test_return_id(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'email@dot.com'
    dto.nickname = 'user'
    dto.birthday = '01.01.2000'
    user_id = repository.create(dto, 'Studio Member')
    assert user_id
    repository.delete(user_id)

def test_missing_nickname(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'email@dot.com'
    dto.birthday = '01.01.2000'
    with pytest.raises(AttributeError):
        repository.create(dto, 'Studio Member')


def test_not_unique_nickname(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'email@dot.com'
    dto.nickname = 'user'
    dto.birthday = '01.01.2000'
    user = repository.create(dto, 'Studio Member')
    with pytest.raises(IntegrityError):
        dto.nickname = 'user'
        user_with_same_name = repository.create(dto, 'Studio Member')
    db.session.rollback()
    repository.delete(user)


def test_role_assignment(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'email@dot.com'
    dto.nickname = 'user'
    dto.birthday = '01.01.2000'
    user_id = repository.create(dto, 'Studio Member')
    user = repository.read(user_id)
    assert db.session.query(Role).filter(Role.role == 'Studio Member').first() in user.role
    repository.delete(user_id)


def test_invalid_email(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'emaildotcom'
    dto.nickname = 'user'
    dto.birthday = '01.01.2000'
    with pytest.raises(ValueError):
        new_user = repository.create(dto, 'Studio Member')


""" read method tests"""
def test_read_successfull(client):
    repository = StudioMemberRepository()
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    assert repository.read(user_id)
    repository.delete(user_id)


def test_read_missing_id(client):
    repository = StudioMemberRepository()
    with pytest.raises(TypeError):
        user = repository.read()

""" read all method tests"""
def test_read_all_successfull(client):
    repository = StudioMemberRepository()
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    user = repository.read(user_id)
    all_users = repository.read_all()
    assert user in all_users
    repository.delete(user_id)


"""update method tests"""
def test_update_successfull(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'email@dot.com'
    dto.nickname = 'user'
    dto.birthday = '01.01.2000'
    user_id = repository.create(dto, 'Studio Member')
    dto.nickname = 'updated_user'
    dto.birthday = '02.02.2002'
    updated_user = repository.update(user_id, dto)
    updated_user = repository.read(user_id)
    assert updated_user.nickname == 'updated_user' and updated_user.birthday == datetime.date(2002, 2, 2)
    repository.delete(user_id)


def test_update_missing_id(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.nickname = 'updated_user'
    dto.birthday = '02.02.2002'
    with pytest.raises(DataError):
        updated_user = repository.update('updated_user', '02.02.2002')


def test_update_missing_dto(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'email@dot.com'
    dto.nickname = 'user'
    dto.birthday = '01.01.2000'
    user_id = repository.create(dto, 'Studio Member')
    with pytest.raises(TypeError):
        updated_user = repository.update(user_id)
    db.session.rollback()
    repository.delete(user_id)


def test_update_set_avatar(client):
    repository = StudioMemberRepository()
    dto = StudioMemberDTO()
    dto.email = 'email@dot.com'
    dto.nickname = 'user'
    dto.birthday = '01.01.2000'
    user_id = repository.create(dto, 'Studio Member')
    avatar = '/home/quastrado/my_learn/Bdays/Bdays/static/img/avas/test_pic.jpeg'
    dto.avatar = avatar
    repository.update(user_id, dto)
    user = repository.read(user_id)
    assert user.avatar == avatar
    db.session.rollback()
    repository.delete(user_id)
    


"""delete method test"""
def test_delete_successfull(client):
    repository = StudioMemberRepository()
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    repository.delete(user_id)
    assert repository.read(user_id) == None


def test_delete_missing_id(client):
    repository = StudioMemberRepository()
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
    repository = StudioMemberRepository()
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    password = 'password'
    incorrect_password = 'passw0rd'
    repository.set_password(user_id, password)
    assert repository.find_studio_member('user', incorrect_password) == None
    repository.delete(user_id)


def test_nonexistent_user(client):
    repository = StudioMemberRepository()
    assert repository.find_studio_member('user', 'password') == None


def test_missing_argument(client):
    repository = StudioMemberRepository()
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    password = 'password'
    repository.set_password(user_id, password)
    with pytest.raises(TypeError):
        repository.find_studio_member('user')
    db.session.rollback()
    repository.delete(user_id)


"""set password method test"""
def test_set_password(client):
    repository = StudioMemberRepository()
    user_id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    model = StudioMember()
    password = 'password'
    repository.set_password(user_id, password)
    user = repository.read(user_id)
    assert user.password and check_password_hash(user.password, password)
    repository.delete(user_id)


def test_missing_id(client):
    repository = StudioMemberRepository()
    password = 'password'
    with pytest.raises(TypeError):
        repository.set_password(password)
