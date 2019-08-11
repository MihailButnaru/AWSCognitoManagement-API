# Copyright 2019
# All rights reserved. Mihail Butnaru
from api.serializers.serializer_factory import factory

class Serializer:
    """
    Generic implementation of the service serializer.
    """
    def serializer(self, serializable, service):
        serializer = factory.get_serializer(service)
        return serializer.serialize(serializable)

serilize = Serializer()