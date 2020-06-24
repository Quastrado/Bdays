import pytest

from tests.test_base import app


def login(client, nickname, password):
    url = '/login/process-login'
    return client.post(url, data={
        'nickname': nickname,
        'password': password
    })


def test_login_successfull(client):
    response = login(client, 'admin', 'aaa')
    assert response.status_code == 200


def test_login_wrong_data(client):
    response = login(client, 'somebody', 'something')
    assert response.status_code == 302


def test_login_miss_nickname(client):
    response = login(client, None, 'aaa')
    assert response.status_code == 400


def test_login_miss_password(client):
    response = login(client, 'admin', None)
    assert response.status_code == 400
