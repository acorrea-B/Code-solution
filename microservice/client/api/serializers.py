from rest_framework import serializers

from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ("id",)


class UpdateClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Client
        fields = "__all__"
