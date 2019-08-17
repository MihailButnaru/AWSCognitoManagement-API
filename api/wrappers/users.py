# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from api.serializers.serializer import serilize
from api.adapters.aws_adapter import init_aws_connection
""" 
User Implementation to get the AWS Cognito Data
"""
class UserManagement():
    """ 
    Cognito User Management Service
    """
    def __init__(self, config):
        """ 
            Args:
                config(str) : configuration parameters
                conn(str) : cognito connector
        """
        self._config = config
        self.aws_conn = init_aws_connection(self._config)
        
    def get_users(self):
        """ 
        Lists the users from the AWS Cognito user pool
        """
        try:
            response = self.aws_conn.list_users(
                UserPoolId=self._config.AWS_USER_POOL_ID
            )
            return serilize.serializer(response['Users'], 'users')
        except Exception as error:
            raise error

    def create_user(self, **kwargs):
        """
        Creates a new user in the specified user pool.
            Args:
                **kwargs (str) :  user parameters
        """
        try:
            response = self.aws_conn.admin_create_user(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                Username=kwargs['username'],
                UserAttributes=[
                    {
                        'Name': 'custom:firstname',
                        'Value': kwargs['firstname']
                    },
                    {
                        'Name': 'custom:surname',
                        'Value': kwargs['surname']
                    },
                    {
                        'Name': 'email',
                        'Value': kwargs['email']
                    }
                ],
                DesiredDeliveryMediums=['EMAIL']
            )
            return response
        except Exception as error:
            raise error

    def get_user(self, username):
        """
        Gets the specified user by user name in a user pool.
        """
        try:
            response = self.aws_conn.admin_get_user(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                Username=username
            )
            return serilize.serializer(response, 'users')
        except Exception as error:
            raise error

    def delete_user(self, username):
        """
        Deletes a user based on the username identifier.
        """
        try:
            response = self.aws_conn.admin_delete_user(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                Username=username
            )
            return response
        except Exception as error:
            raise error

    def edit_user(self, **kwargs):
        """
        Updates the specified user attributes
        """
        try:
            response = self.aws_conn.admin_update_user_attributes(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                Username=kwargs['username'],
                UserAttributes=[
                    {
                        'Name': 'custom:firstname',
                        'Value': kwargs['firstname']
                    },
                    {
                        'Name': 'custom:surname',
                        'Value': kwargs['surname']
                    },
                    {
                        'Name': 'email',
                        'Value': kwargs['email']
                    }
                ]
            )
            return response
        except Exception as error:
            raise error
