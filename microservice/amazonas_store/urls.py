from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import include
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from location.api.api_urls import urlpatterns as location
from store.api.api_urls import urlpatterns as store
from client.api.api_urls import urlpatterns as client

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Amazonas store",
        default_version="1.0.0",
        description="API documentation",
    ),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                path("client/", include(client)),
                path("location/", include(location)),
                path("store/", include(store)),
                path(
                    "swagger/",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="swagger-schema",
                ),
            ]
        ),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
