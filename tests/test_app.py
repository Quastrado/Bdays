import pytest
import uuid

from sqlalchemy.exc import IntegrityError

from Bdays import create_app
from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.DAL.models.roles import Role
from Bdays.DAL.studio_member_repository import StudioMemberRepository

repository = StudioMemberRepository()


@pytest.fixture
def app():
    app=create_app(test_config=True)
    return app


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
    