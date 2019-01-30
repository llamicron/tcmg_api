import pytest

from .server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()


def test_md5(client):
    r = client.get('/md5/hash this please')
    assert b'f211faadbeacebe3ed95f3fc8116449a' in r.data
