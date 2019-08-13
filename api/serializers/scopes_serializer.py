# Copyright 2019 by Mihail Butnaru
# All rights reserved.
"""
Serializer that formats the correct data of the scopes from
the user pool. AWS API does not handle the serialization.
"""
class ScopesSerializer:
    """
    Scope serializer, handles the data from the api,
    unclean data is serialized in the correct format
    """
    def serialize(self, scopes):
        """
            Args:
                scopes (list): list of resouce servers
        """
        scope = []
        for scp in scopes['ResourceServers']:
            content = {}
            content['name'] = scp['Name'] + '/' + scp['Scopes'][0]['ScopeName']
            scope.append(content)
        return {'Scopes' : scope }

