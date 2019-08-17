# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from tests.mock_data import scope

def test_get_scopes(api_client):
    """
    Ensures that all the scoes are returned
    """
    response = api_client.get('api/v1/scopes/')
    assert response.status_code == 200

def test_create_scope(api_client, scope):
    """
    Ensure that the correct scope was created
    """
    response = api_client.post('/api/v1/scopes/', json=scope)
    assert response.status_code == 201

def test_delete_scope(api_client, scope):
    """
    Ensure that the correct scope was deleted
    """
    identifier = scope['identifier']
    response = api_client.delete(f'/api/v1/scopes/{identifier}')
    assert response.status_code == 200