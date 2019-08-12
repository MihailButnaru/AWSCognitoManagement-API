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

    def create_app_client(self):
        """
        """
        pass

    def get_app_client(self):
        """
        """
        pass

    def edit_app_client(self):
        """
        """
        pass

    def delete_app_client(self):
        """
        """
        pass