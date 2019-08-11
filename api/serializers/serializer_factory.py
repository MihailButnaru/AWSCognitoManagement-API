# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from api.serializers.users_serializer import UserSerializer


class SerializerFactory:
    """
    Serializer Interface, customize the behaviour
    based on the different type of the serialize object.
    """
    def get_serializer(self, service):
        """
        It evaluates the value of the service and decides
        the concrete implementation to create and return.
            Args:
                service (str): type of the service
        """
        if service == 'users':
            return UserSerializer()
        elif service == 'apiclients':
            pass
        elif service == 'scopes':
            pass
        else:
            raise ValueError(service)

factory = SerializerFactory()
