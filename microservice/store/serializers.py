from rest_framework import serializers

from store.models import Store


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name", "code")
        read_only_fields = ("id",)


class UpdateStoreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Store
        fields = "__all__"
