""" Tests the AWS connection with the credentials from the config file. """
import boto3
from api.config import Config

def test_connection():
    """AWS Cognito Connection test."""
    _config = Config()
    test_connection = boto3.client(
        _config.AWS_SERVICE,
        aws_access_key_id=_config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=_config.AWS_SECRET_ACCESS_KEY,
        region_name=_config.AWS_REGION_NAME
    )
