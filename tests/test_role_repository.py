import pytest
import uuid

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
