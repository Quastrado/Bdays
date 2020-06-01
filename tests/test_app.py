import pytest
from Bdays import create_app


@pytest.fixture
def app():
    app=create_app()
    return app


def test_app(client):
    response = client.get('/')
    assert response.status_code == 200