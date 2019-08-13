# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask_restplus import fields
from api.routes.restplus import api

namespace = api.namespace('scopes', description='Scopes Management operations.')

scope_model = api.model('Scopes', {
    'identifier': fields.String(
        required=True,
        description='A unique resource server identifier'
    ),
    'name': fields.String(
        required=True,
        description='Name for the resource server'
    ),
    'scopeName': fields.String(
        required=True,
        description='The name of the scope'
    ),
    'scopeDescription': fields.String(
        required=True,
        description='The description of the scope'
    )
})