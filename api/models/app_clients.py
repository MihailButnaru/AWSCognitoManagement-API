# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask_restplus import fields
from api.routes.restplus import api

namespace = api.namespace('appclients', description='App Clients Management operations.')

app_client_model = api.model('AppClients', {
    'id': fields.String(
        readOnly=True,
        default='Unique Identifier is stored in the mongodb',
        description='The Client unique identifier'
    ),
    'name': fields.String(
        required=True,
        description='Client name'
    )
})