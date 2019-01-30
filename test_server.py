import json

import pytest

from .server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()


def test_md5(client):
    r = client.get('/md5/hash this please')
    data = json.loads(str(r.data))

    assert data['output'] == 'f211faadbeacebe3ed95f3fc8116449a'

def test_factorial(client):
    r = client.get('/factorial/7')
    data = json.loads(str(r.data))

    assert data['output'] == 5040

    r = client.get('/factorial/-4')
    data = json.loads(str(r.data))

    assert data['output'] == 'Error: integer needs to be positive'

def test_fib(client):
    r = client.get('/fibonacci/20')
    data = json.loads(str(r.data))

    assert data['output'] == [0, 1, 1, 2, 3, 5, 8, 13]

    r = client.get('/fibonacci/-4')
    data = json.loads(str(r.data))

    assert data['output'] == 'Error: integer needs to be positive'
