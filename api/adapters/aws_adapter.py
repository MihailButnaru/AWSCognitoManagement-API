# Copyright 2019
# All rights reserved. Mihail Butnaru
""" Enables to create a connection to access
AWS services.
"""
import logging
import boto3

class AWSConnection():
    """ Easy use connection through the boto3 to access
    AWS Services.
    """
    def __init__(self, config):
        """ Boto3 client connection based on the configuration.
            Args:
                config (str): config parameters
        """
        self.conn = boto3.client(
            config.AWS_SERVICE,
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_accesS_key=config.AWS_SECRET_ACCESS_KEY,
            region_name=config.AWS_REGION_NAME
        )

