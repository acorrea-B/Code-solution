from django.urls import path

from location.api.views.country_view import CountryView

urlpatterns = [
    path(
        "country/",
        CountryView.as_view(),
    ),
]
