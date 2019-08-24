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
        if isinstance(users, list):
            return self.serialize_users(users)
        else:
            return self.serialize_user(users)

    def serialize_users(self, users):
        attributes = []
        for user in users:
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

    def serialize_user(self, user):
        content = {}
        content['username'] = user['Username']
        for attr in user['UserAttributes']:
            if attr['Name'] == 'custom:firstname':
                content['firstname'] = attr['Value']
            elif attr['Name'] == 'custom:surname':
                content['surname'] = attr['Value']
            elif attr['Name'] == 'email':
                content['email'] = attr['Value']
        return content

