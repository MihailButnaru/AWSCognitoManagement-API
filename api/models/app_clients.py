# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask_restplus import fields
from api.routes.restplus import api

namespace = api.namespace('appclients', description='App Clients Management operations.')

app_client_model = api.model('AppClients', {
    'name': fields.String(
        required=True,
        description='Client name'
    ),
    'scope': fields.String(
        required=True,
        description='Scope of the app'
    )
})