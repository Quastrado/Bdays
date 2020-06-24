import pytest
import json

from flask import url_for

from Bdays import create_app


@pytest.fixture
def app():
    app = create_app(test_config=True)
    return app


def test_example(client):
    response = client.get("/")
    assert response.status_code == 200
