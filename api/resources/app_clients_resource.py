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
        pass