# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask import request, jsonify
from flask_restplus import Resource
from api.models.app_clients import namespace as ns
from api.models.app_clients import app_client_model
from api.wrappers import app_client_manager

@ns.route('/', resource_class_kwargs={'app_client_manager': app_client_manager})
class AppClientsList(Resource):
    """
    Lists the clients that have been created for the specified
    identity provider.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_client_manager = kwargs['app_client_manager']

    @ns.marshal_list_with(app_client_model)
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def get(self):
        """
        Returns a list of clients
        """
        return self.app_client_manager.get_app_clients(), 200

    @ns.expect(app_client_model)
    @ns.marshal_with(app_client_model, code=201)
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def post(self):
        """
        Creates a new app client
        """
        try:
            payload = request.get_json(force=True)
            self.app_client_manager.create_app_client(**payload)
            return payload, 201
        except Exception as error:
            raise error

@ns.route('/<clientId>',  resource_class_kwargs={'app_client_manager': app_client_manager})
class AppClients(Resource):
    """
    Shows a single app client and lets you delete the app client
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_client_manager = kwargs['app_client_manager']

    @ns.response(200, 'Success')
    @ns.response(403, 'Validation Error')
    def get(self, clientId):
        """
        Get's the specific client based on the clientId
        """
        try:
            return self.app_client_manager.get_app_client(clientId), 200
        except Exception:
            raise ValueError('AppClient with the specified Id does not exist!')

    @ns.response(200, 'Success')
    def delete(self, clientId):
        """
        Delete a client based on the clientId
        """
        try:
            return self.app_client_manager.delete_app_client(clientId), 200
        except Exception:
            raise ValueError('AppClient with the specified Id does not exist!')