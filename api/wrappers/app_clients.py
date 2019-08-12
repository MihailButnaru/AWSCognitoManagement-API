# Copyright 2019 by Mihail Butnaru
# All rights reserved.
import json
from api.adapters.aws_adapter import init_aws_connection
from api.serializers.serializer import serilize
"""
App Clients are entities within a user environment[pool] that
has different permissions to call for accessing different resources.
"""
class AppClientsManagement():
    """
    AppClients Management Service
    """
    def __init__(self, config):
        """
            Args:
                config(str): configuration parameters
        """
        self._config = config
        self._aws_conn = init_aws_connection(self._config)

    def get_app_clients(self):
        """
        Lists the clients that have been created
        """
        try:
            response = self._aws_conn.list_user_pool_clients(
                UserPoolId=self._config.AWS_USER_POOL_ID
            )
            return serilize.serializer(response, 'appclients')
        except Exception as error:
            raise error

    def create_app_client(self, **kwargs):
        """
        Creates the user pool based on custom parameters
        """
        try:
            response = self._aws_conn.create_user_pool_client(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                ClientName=kwargs['name'],
                GenerateSecret=True,
                ReadAttributes=[
                    'custom:firstname',
                    'custom:surname',
                    'email'
                ],
                AllowedOAuthFlows=['client_credentials'],
                AllowedOAuthScopes=[kwargs['scope']],
                AllowedOAuthFlowsUserPoolClient=True
            )
            return response
        except Exception as error:
            raise error

    def get_app_client(self, client_id):
        """
        Returns the configuration information and metadata of
        the specified app client
        """
        try:
            response = self._aws_conn.describe_user_pool_client(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                ClientId=client_id
            )
            response['UserPoolClient']['LastModifiedDate'].isoformat()
            response['UserPoolClient']['CreationDate'].isoformat()
            return response
        except Exception as error:
            raise error 

    def delete_app_client(self, client_id):
        """
        Deletes the user pool based on the clientId
        """
        try:
            response = self._aws_conn.delete_user_pool_client(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                ClientId=client_id
            )
            return response
        except Exception as error:
            raise error