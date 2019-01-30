import json

import pytest

from server import app

def get(uri):
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.get(uri)
    return json.loads(response.data.decode('utf-8'))


def test_md5():
    data = get('/md5/hash this please')

    assert data['output'] == 'f211faadbeacebe3ed95f3fc8116449a'

def test_factorial():
    data = get('/factorial/7')

    assert data['output'] == 5040

    data = get('/factorial/-4')

    assert data['output'] == 'Error: integer needs to be positive'

def test_fib():
    data = get('/fibonacci/20')

    assert data['output'] == [0, 1, 1, 2, 3, 5, 8, 13]

    data = get('/fibonacci/-4')

    assert data['output'] == 'Error: integer needs to be positive'

