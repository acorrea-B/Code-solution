from django.urls import path

from location.api.views.country_view import CountryView
from location.api.views.state_view import StateView

urlpatterns = [
    path(
        "country/",
        CountryView.as_view(),
    ),
    path(
        "state/",
        StateView.as_view(),
    ),
]
