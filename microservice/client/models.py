from django.db import models

from location.models import Country
from location.models import State
from location.models import City
from store.models import Store


class Client(models.Model):
    name = models.CharField(max_length=200)
    sumame = models.CharField(max_length=200)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="country"
    )
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="state")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city")
    favorite_store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name="store"
    )
