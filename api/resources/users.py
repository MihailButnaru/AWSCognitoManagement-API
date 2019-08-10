# Copyright 2019 by Mihail Butnaru
# All rights reserved.
import logging
from flask import request
from flask_restplus import Resource
from api.routes.restplus import api
from api.models.users import namespace as ns


ns.route('/')
class UserList(Resource):
    """ Shows a list of all the users, and lets
    you POST to add a new user.
    """
    @ns.doc('list_users')
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def get(self):
        """ List all users """
        pass

    @ns.doc('create_user')
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def post(self):
        """ Create a new user """
        pass


