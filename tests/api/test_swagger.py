# Copyright 2019 by Mihail Butnaru
# All rights reserved.

def test_swagger_resource_type(api_client):
    response = api_client.get('api/v1/swagger.json')
    assert response.status_code == 200