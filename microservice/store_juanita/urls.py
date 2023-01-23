from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import include
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from location.api_urls import urlpatterns as location
from store.api_urls import urlpatterns as store

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Amazonas store_juanita",
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
