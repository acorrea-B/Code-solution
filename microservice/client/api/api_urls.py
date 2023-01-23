from django.urls import path

from client.api.views.client_view import ClientView


urlpatterns = [
    path(
        "",
        ClientView.as_view(),
    ),
]
