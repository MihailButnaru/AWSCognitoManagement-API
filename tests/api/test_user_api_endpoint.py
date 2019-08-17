# Copyright 2019 by Mihail Butnaru
# All rights reserved.
import json
from tests.mock_data import user

def test_get_users(api_client):
    """
    Ensure's that getting all the users from the root 
    /users returns the correct response code
    """
    response = api_client.get('api/v1/users/')
    assert response.status_code == 200

def test_create_user(api_client, user):
    """
    Ensure that the endpoints /users creates the correct
    user and returns the correct data
    """
    response = api_client.post('/api/v1/users/', json=user)
    assert response.json == user
    assert response.status_code == 201

def test_edit_user(api_client, user):
    """
    Ensure that the endpoint /users/{username} updates
    the correct user give the username based on the new data
    """
    username = user['username']
    user['firstname'] = 'Michael'
    response = api_client.put(f'/api/v1/users/{username}', json=user)
    assert response.json == user
    assert response.status_code == 200

def test_delete_user(api_client, user):
    """
    Ensure that the endpoint /users/{username} deletes
    the correct user given the correct username
    """
    username = user['username']
    response = api_client.delete(f'/api/v1/users/{username}')
    assert response.status_code == 200

