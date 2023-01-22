from rest_framework import serializers

from models import State
from country_serializer import CountrySerializerResponse


class StateSerializerRequest(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ("name", "code", "country")


class StateSerializerResponse:
    country = CountrySerializerResponse(read_only=True)

    class Meta:
        model = State
        fields = ("id", "name", "code", "country")
