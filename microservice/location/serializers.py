from rest_framework import serializers

from location.models import Country
from location.models import State
from location.models import City


class CountrySerializerRequest(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        read_only_fields = ("id",)


class UpdateCountrySerializerRequest(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Country
        fields = ("id", "name", "code")


class CountrySerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StateSerializerRequest(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ("name", "code", "country")


class StateSerializerResponse(serializers.HyperlinkedModelSerializer):
    country = CountrySerializerResponse(read_only=True)

    class Meta:
        model = State
        fields = ("id", "name", "code", "country")


class CitySerializerRequest(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ("name", "code", "state")


class CitySerializerResponse(serializers.HyperlinkedModelSerializer):
    state = StateSerializerResponse(read_only=True)

    class Meta:
        model = City
        fields = ("id", "name", "code", "state")
