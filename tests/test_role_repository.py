import pytest
import uuid

from sqlalchemy.exc import DataError, ProgrammingError

from tests.test_base import app
from Bdays.DAL.models.db import db
from Bdays.DAL.models.roles import Role
from Bdays.DAL.role_repository import RoleRepository

repository = RoleRepository()


"""create method tests"""
def test_create_successfull(client):
    id = uuid.uuid4()
    role_name = 'Tester'
    repository.create(role_name, id)
    assert repository.read(id)
    repository.delete(id)


def test_create_without_id(client):
    role_name = 'Tester'
    role_id = repository.create(role_name)
    assert repository.read(role_id)
    repository.delete(role_id)


def test_create_missing_role(client):
    with pytest.raises(TypeError):
        repository.create()


def test_create_incorrect_id(client):
    id = 123
    role_name = 'Tester'
    with pytest.raises(DataError):
        repository.create(id, role_name)


def test_create_incorrect_role(client):
    role_name = 123
    role_id = repository.create(role_name)
    assert repository.read(role_id)
    repository.delete(role_id)


"""read method tests"""
def test_read_successfull(client):
    role_name = 'Tester'
    role_id = repository.create(role_name)
    assert repository.read(role_id)
    repository.delete(role_id)


def test_read_missing_id(client):
    with pytest.raises(TypeError):
        repository.read()


def test_read_incorrect_id(client):
    id = 123
    with pytest.raises(ProgrammingError):
        repository.read(id)


"""read all method tests"""
def test_read_all_successfull(client):
    role_name = 'Tester'
    role_id = repository.create(role_name)
    new_role = repository.read(role_id)
    assert new_role in repository.read_all()
    repository.delete(role_id)


"""update method test"""
def test_update_role_name_successfull(client):
    role_name = 'Tester'
    role_id = repository.create(role_name)
    repository.update(role_id, 'Another Role')    
    assert repository.read(role_id).role == 'Another Role'
    repository.delete(role_id)


def test_update_missing_id(client):
    role_name = 'Tester'
    role_id = repository.create(role_name)
    with pytest.raises(TypeError):
        repository.update('Another Role')
    db.session.rollback()
    repository.delete(role_id)


def test_update_missing_role_name(client):
    role_name = 'Tester'
    role_id = repository.create(role_name)
    with pytest.raises(TypeError):
        repository.update(role_id)
    db.session.rollback()
    repository.delete(role_id)


def test_update_change_of_argument_places(client):
    role_name = 'Tester'
    role_id = repository.create(role_name)
    with pytest.raises(DataError):
        repository.update(role_name, role_id)
    db.session.rollback()
    repository.delete(role_id)
