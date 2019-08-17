# Copyright 2019 by Mihail Butnaru
# All rights reserved.

def test_root(api_client):
    """
    Ensure that API root returns OK response code
    and that the response endpint is the default 'api/v1'
    """
    response = api_client.get('api/v1/')
    assert response.status_code == 200