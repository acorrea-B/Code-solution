from django.urls import path

from location.api.views.country_view import CountryView
from location.api.views.state_view import StateView
from location.api.views.city_view import CityView

urlpatterns = [
    path(
        "country/",
        CountryView.as_view(),
    ),
    path(
        "country/state/",
        StateView.as_view(),
    ),
    path(
        "country/state/city/",
        CityView.as_view(),
    ),
]
