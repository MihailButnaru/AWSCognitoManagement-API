# Copyright 2019 by Mihail Butnaru
# All rights reserved.
import json
from api.config import Config
from api.serializers.serializer import serilize
""" User Implementation to get the AWS Cognito Data
"""
class CognitoUserManagement():
    """ Cognito User Management Service
    """
    def __init__(self, config, conn):
        """ 
            Args:
                config(str) : configuration parameters
                conn(str) : cognito connect
        """
        self._config = config
        self.aws_conn = conn
        
    def get_users(self):
        """ 
        Lists the users from the AWS Cognito user pool
        """
        try:
            response = self.aws_conn.list_users(
                UserPoolId=self._config.AWS_USER_POOL_ID
            )
            return serilize.serializer(response, 'users')
        except Exception as error:
            raise error

