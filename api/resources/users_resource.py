# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask import request, jsonify
from flask_restplus import Resource
from api.routes.restplus import api
from api.models.users import namespace as ns
from api.models.users import user_model
from api.wrappers import user_manager

@ns.route('/', resource_class_kwargs={'user_manager': user_manager})
class UserList(Resource):
    """ Shows a list of all the users, and lets
    you POST to add a new user.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_manager = kwargs['user_manager']

    @ns.marshal_list_with(user_model)
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def get(self):
        """ List all users """
        return self.user_manager.get_users(), 200

    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def post(self):
        """ Create a new user """
        try:
            payload = request.get_json(force=True)
            self.user_manager.create_user(**payload)
            return payload, 201
        except Exception as error:
            raise error
        

@ns.route('/<username>', resource_class_kwargs={'user_manager': user_manager})
class User(Resource):
    """ Show a single user item and lets you delete the user
    or edit the user.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_manager = kwargs['user_manager']

    @ns.marshal_with(user_model)
    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    def get(self, username):
        """ 
        Get's the specific user based on the username.
        """
        try: 
            return self.user_manager.get_user(username), 200
        except Exception:
            raise ValueError('User not found!')

    @ns.response(200, 'Success')
    def delete(self, username):
        """
        Delete a user given its username as an identifier.
        """
        try:
            self.user_manager.delete_user(username)
            return {'message': 'User was deleted successful'}, 200
        except Exception as error:
            raise error

    # @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, username):
        """
        Update a user given its username as an identifier.
        """
        try:
            payload = request.get_json(force=True)
            self.user_manager.edit_user(**payload)
            return payload, 200
        except Exception as error:
            raise error

    