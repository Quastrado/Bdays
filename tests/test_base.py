import pytest

from Bdays import create_app


@pytest.fixture
def app():
    app=create_app(test_config=True)
    return app