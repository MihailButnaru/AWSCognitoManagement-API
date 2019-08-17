"""
Mock data used to test the API
"""
import pytest

@pytest.fixture
def user():
    data = {
        'username': 'andrewS',
        'firstname': 'Andrew',
        'surname': 'Smith',
        'email': 'asmith@hotmail.com'
    }
    return data

@pytest.fixture
def app_client():
    data = {
        'name': 'TestApi',
        'scope': 'saga/*'
    }
    return data

@pytest.fixture
def scope():
    data = {
        'identifier': '0110',
        'name': 'TestAp',
        'scopeName': 'api',
        'scopeDescription': '*'
    }
    return data