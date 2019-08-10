# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from api.config import Config
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
            for users in response['Users']:
                users['UserCreateDate'] = users['UserCreateDate'].isoformat()
                users['UserLastModifiedDate'] = users['UserLastModifiedDate'].isoformat()
            return response
        except Exception as error:
            raise error

