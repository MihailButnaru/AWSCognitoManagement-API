# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask_restplus import fields
from api.routes.restplus import api

namespace = api.namespace('users', description='Users Management operations.')

user_model = api.model('Users', {
    'username': fields.String(
        required=True,
        description='Username of the user.'
    ),
    'firstname': fields.String(
        required=True,
        description='The Firstname of the user'
    ),
    'surname': fields.String(
        required=True,
        description='The Surname of the user'
    ),
    'email': fields.String(
        required=True,
        description='Email of the user'
    )
})