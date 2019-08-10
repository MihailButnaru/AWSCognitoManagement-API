# Copyright 2019
# All rights reserved. Mihail Butnaru
""" Enables to create a connection to access
AWS services.
"""
import logging
import boto3
from api.config import Config

class AWSConnection():
    """ Easy use connection through the boto3 to access
    AWS Services.
    """
    def __init__(self):
        """ Boto3 client connection based on the configuration.
            Args:
                config (str): config parameters
        """
        self.config = Config()
        self.client = boto3.client(
            self.config.AWS_SERVICE,
            aws_access_key_id=self.config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=self.config.AWS_SECRET_ACCESS_KEY,
            region_name=self.config.AWS_REGION_NAME
        )
