from rest_framework import serializers

from models import Country


class CountrySerializerRequest(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ("name", "code")


class CountrySerializerResponse:
    class Meta:
        model = Country
        fields = ("id", "name", "code")
