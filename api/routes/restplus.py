# Copyright 2019
# All rights reserved. Mihail Butnaru
"""
RestPlus provides information about the API
Must be initialized with a Flask Application.
"""
import logging
from flask_restplus import Api

logger = logging.getLogger(__name__)

api = Api(
    version='1.0',
    title='AWS Cognito Management Restful API',
    description='Cognito Management API, allows you to manage users/appclients resources.'
    )

@api.errorhandler
def default_error_handler(error):
    """
    Registers a default error handler when an exception occured.
    """
    message = 'An unhandled exception occured.'
    logger.exception(message)
    return {'message': message}, 500
