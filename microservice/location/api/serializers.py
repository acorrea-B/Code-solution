from rest_framework import serializers

from location.models import Country
from location.models import State
from location.models import City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        read_only_fields = ("id",)


class UpdateCountry(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Country
        fields = ("id", "name", "code")


class StateSerializer(serializers.ModelSerializer):

    country = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Country.objects.all()
    )

    class Meta:
        model = State
        fields = ("id", "name", "code", "country")
        read_only_fields = ("id",)
        depth = 1


class UpdateStateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = State
        fields = "__all__"


class CitySerializer(serializers.HyperlinkedModelSerializer):
    state = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=State.objects.all()
    )

    class Meta:
        model = City
        fields = ("id", "name", "code", "state")
        read_only_fields = ("id",)
        depth = 1


class UpdateCitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = City
        fields = "__all__"
