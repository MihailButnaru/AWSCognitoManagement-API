# Copyright 2019 by Mihail Butnaru
# All rights reserved.
import logging
from api.routes.restplus import api
from flask import Flask, Blueprint
from api.resources.users import ns as users_namespace


def create_app(config):
    """ Flask Initialization application
    """
    logging.getLogger(__name__)

    # Flask
    app = Flask(__name__)

    # Swagger configuration
    app.config['SWAGGER_UI_DOC_EXPANSION'] = config.SWAGGER_UI_DOC_EXPANSION
    app.config['RESTPLUS_MASK_SWAGGER'] = config.RESTPLUS_MASK_SWAGGER
    app.config['RESTPLUS_VALIDATION'] = config.RESTPLUS_VALIDATE
    app.config['RESSTPLUS_ERROR_404_HELP'] = config.RESTPLUS_ERROR_404_HELP

    # Initialize
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(users_namespace)
    app.register_blueprint(blueprint)

    return app