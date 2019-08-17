# Copyright 2019 by Mihail Butnaru
# All rights reserved.
"""
Serializer that formats the correct data from the API
"""
class AppClientSerializer:
    """
    AppClientSerializer, serializes data from the API
    """
    def serialize(self, app_clients):
        """
        Serializer
            Args:
                app_clients (list): list of app clients
        Due to the privacy the AppClientID it will be stored just in the datastore
        """
        clients = []
        for client in app_clients['UserPoolClients']:
            content = {}
            content['name'] = client['ClientName']
            clients.append(content)
        return {'Clients' : clients}
