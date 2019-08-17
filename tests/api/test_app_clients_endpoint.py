# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from tests.mock_data import app_client

def test_get_app_clients(api_client):
    """
    Ensures that the endpoint appclients returns
    the correct data.
    """
    response = api_client.get('/api/v1/appclients/')
    assert response.status_code == 200

def test_create_app_client(api_client, app_client):
    """
    Ensures that the endpoint /appclients creates
    a new app client based on the mock data.
    """
    response = api_client.post('/api/v1/appclients/', json=app_client)
    assert response.status_code == 201