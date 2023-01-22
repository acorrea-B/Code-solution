from rest_framework import serializers

from models import City
from state_serializer import StateSerializerResponse


class CitySerializerRequest(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ("name", "code", "state")


class CitySerializerResponse:
    state = StateSerializerResponse(read_only=True)

    class Meta:
        model = City
        fields = ("id", "name", "code", "state")
