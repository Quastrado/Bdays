import uuid
import pytest
from Bdays import create_app
from Bdays.DAL.models.db import db
from Bdays.DAL.models.studio_member import StudioMember
from Bdays.DAL.studio_member_repository import StudioMemberRepository


@pytest.fixture
def app():
    app=create_app(test_config=True)
    return app


def test_studio_member_create_successfull(client):
    repository = StudioMemberRepository()
    id = repository.create('email@dot.com', 'user', '01.01.2000', 'Studio Member')
    assert StudioMember.query.filter_by(nickname='user').first()
    repository.delete(id)


def test_missing_argument(client):
    repository = StudioMemberRepository()
    with pytest.raises(TypeError):
        repository.create('email1@dot.com', '01.01.2000', 'Studio Member')




