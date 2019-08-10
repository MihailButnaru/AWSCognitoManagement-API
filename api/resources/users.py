# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask import request
from flask_restplus import Resource
from api.routes.restplus import api
from api.models.users import namespace as ns
from api.models.users import user_model


@ns.route('/')
class UserList(Resource):
    """ Shows a list of all the users, and lets
    you POST to add a new user.
    """
    @ns.marshal_list_with(user_model)
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def get(self):
        """ List all users """
        pass

    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def post(self):
        """ Create a new user """
        pass


