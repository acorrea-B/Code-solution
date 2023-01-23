from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=400)
    code = models.CharField(max_length=2)


class State(models.Model):
    name = models.CharField(max_length=400)
    code = models.CharField(max_length=4)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="country"
    )


class City(models.Model):
    name = models.CharField(max_length=400)
    code = models.CharField(max_length=8)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
