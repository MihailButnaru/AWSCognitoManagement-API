# Copyright 2019 by Mihail Butnaru
# All rights reserved.
"""
Conftest used to import external plugins or modules.
"""
import pytest
from flask import Response, json
from flask.testing import FlaskClient

from api.app import create_app
from api.config import Config

@pytest.fixture
def app():
    """
    Set up global app for functional tests
    """
    _config = Config()
    app = create_app(_config)
    app.test_client = ApiClient
    app.response = ApiResponse
    return app


class ApiClient(FlaskClient):
    def open(self, *args, **kwargs):
        json_data = kwargs.pop('json', None)

        if json_data is not None:
            kwargs['data'] = json.dumps(json_data)
            kwargs['content-type'] = 'application/json'
        return super(ApiClient, self).open(*args, **kwargs)

class ApiResponse(Response):
    @property
    def json(self):
        return json.loads(self.data)

@pytest.fixture
def api_client(client):
    return client.test_client