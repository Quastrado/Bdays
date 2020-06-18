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
    role = 'Tester'
    repository.create(role, id)
    assert repository.read(id)
    repository.delete(id)


def test_create_without_id(client):
    role = 'Tester'
    role_id = repository.create(role)
    assert repository.read(role_id)
    repository.delete(role_id)


def test_create_missing_role(client):
    with pytest.raises(TypeError):
        repository.create()


def test_create_incorrect_id(client):
    id = 123
    role = 'Tester'
    with pytest.raises(DataError):
        repository.create(id, role)


def test_create_incorrect_role(client):
    role = 123
    role_id = repository.create(role)
    assert repository.read(role_id)
    repository.delete(role_id)


"""read method tests"""
def test_read_successfull(client):
    role = 'Tester'
    role_id = repository.create(role)
    assert repository.read(role_id)
    repository.delete(role_id)


def test_read_missing_id(client):
    with pytest.raises(TypeError):
        repository.read()


def test_read_incorrect_id(client):
    id = 123
    with pytest.raises(ProgrammingError):
        repository.read(id)
        