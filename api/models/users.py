# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask_restplus import fields
from api.routes.restplus import api

namespace = api.namespace('users', description='Users operations.')
