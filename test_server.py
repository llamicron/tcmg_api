import json

import pytest

try:
    from .server import app, valid_number
except ImportError:
    from server import app, valid_number

def get(uri):
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.get(uri)
    return json.loads(response.data.decode('utf-8'))


def test_valid_number():
    assert valid_number('4')
    assert valid_number('1')
    assert valid_number('412376234')
    assert not valid_number('-14')
    assert not valid_number('0')

def test_md5():
    data = get('/md5/hash this please')
    assert data['output'] == 'f211faadbeacebe3ed95f3fc8116449a'

def test_factorial():
    data = get('/factorial/7')
    assert data['output'] == 5040

    data = get('/factorial/-4')
    assert data['output'] == 'Error: not a valid number'

    data = get('/factorial/some string lmao')
    assert data['output'] == 'Error: not a valid number'

def test_fib():
    data = get('/fibonacci/20')
    assert data['output'] == [0, 1, 1, 2, 3, 5, 8, 13]

    data = get('/fibonacci/-4')
    assert data['output'] == 'Error: not a valid number'

    data = get('/fibonacci/a string here')
    assert data['output'] == 'Error: not a valid number'


def test_is_prime():
    data = get('/is-prime/7')
    assert data['output'] == True

    data = get('/is-prime/-4')
    assert data['output'] == 'Error: not a valid number'

    data = get('/is-prime/a string')
    assert data['output'] == 'Error: not a valid number'

def test_slack_message():
    data = get('/slack-alert/testing!')
    assert data['output'] == True
