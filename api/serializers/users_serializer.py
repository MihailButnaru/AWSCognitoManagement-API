# Copyright 2019 by Mihail Butnaru
# All rights reserved.

class UserSerializer:
    """
    UserSerializer format to the model list of the API Json.
    """ 
    def serialize(self, users):
        """
        Serializer
            Args:
                users (list) : list of users
        """
        attributes = []
        for user in users['Users']:
            content = {}
            content['username'] = user['Username']
            for attr in user['Attributes']:
                if attr['Name'] == 'custom:firstname':
                    content['firstname'] = attr['Value']
                elif attr['Name'] == 'custom:surname':
                    content['surname'] = attr['Value']
                elif attr['Name'] == 'email':
                    content['email'] = attr['Value']
            attributes.append(content)
        return attributes
        
