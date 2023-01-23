from django.db import models

from location.models import Country
from location.models import State
from location.models import City
from store.models import Store


class Client(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="client_country"
    )
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="client_state"
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="client_city")
    favorite_store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name="client_store"
    )
