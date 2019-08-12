# Copyright 2019
# All rights reserved. Mihail Butnaru
""" 
Creates a connection to access AWS services.
"""
import logging
import boto3

def init_aws_connection(config):
    """
    AWS connection through Boto3 to access AWS Services.
        Args:
            config (str): config parameters
    """
    _log = logging.getLogger(__name__)

    return boto3.client(
        config.AWS_SERVICE,
        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        region_name=config.AWS_REGION_NAME
    )
