import pytest
from ..__main__ import start


@pytest.fixture
def app():
    instance = start()
    return instance
