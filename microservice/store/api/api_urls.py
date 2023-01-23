from django.urls import path

from store.api.views.store_view import StoreView


urlpatterns = [
    path(
        "",
        StoreView.as_view(),
    ),
]
