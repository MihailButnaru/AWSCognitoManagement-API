# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from api.adapters.aws_adapter import init_aws_connection
from api.serializers.serializer import serilize
"""
Scopes are levels of access that an app can request to a resource. A resource
server is a server for access-protected resources. It handles
authenticated requests from an app that has an access token.
"""
class ScopesManagement():
    """
    Scope Management handles the create, delete, view the resources
    of the specified user pool, as well as it allows to define
    two scopes: one for read access and one for write/delete access.
    """
    def __init__(self, config):
        """
            Args:
                config(str): configuration parameters
        """
        self._config = config
        self._aws_conn = init_aws_connection(self._config)

    def get_scopes(self):
        """
        Lists the resources servers [scopes] for a user pool
        specified in the configuration file.
        """
        try:
            response = self._aws_conn.list_resource_servers(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                MaxResults=50 # 50 is the default value
            )
            return serilize.serializer(response, 'scopes')
        except Exception as error:
            raise error

    def create_scope(self, **kwargs):
        """
        Creates OAuth 2.0 resource server that defines custom scope in it.
            Args:
                identifier (str): a unique resource server identifier
                name (str): a friendly name for the resource server
                scopeName (str): the name of the scope
                scopeDescription (str): the description of the scope
        """
        try:
            response = self._aws_conn.create_resource_server(
                UserPoolId=self._config.AWS_USER_POOL_ID,
                Name=kwargs['name'],
                Identifier=kwargs['identifier'],
                Scopes=[
                    {
                        'ScopeName': kwargs['scopeName'],
                        'ScopeDescription': kwargs['scopeDescription']
                    }
                ]
            )
            return response
        except Exception as error:
            raise error
