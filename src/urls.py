from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions  # new
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi

# Django admin settings
admin.site.site_header = "Get on Space"
admin.site.index_title = "Admin Dashboard"

# API information for schema view
api_info = openapi.Info(
    title="Expense Tracker",
    default_version="v1",
    description="An expense tracking API",
    terms_of_service="https://davidkinyanjui052@gmail.com",
    contact=openapi.Contact(email="davidkinyanjui052@gmail.com"),
    license=openapi.License(name="MIT License"),
)

# Schema view configuration
schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns
urlpatterns = [
    # Django admin URLs
    path("admin/", admin.site.urls),
    # API routes
    path("api/v1/", include("modules.api.urls")),
    # API documentation
    path(
        "api/v1/docs/",
        include_docs_urls(
            title="Expense Tracker API",
            description="API documentation for the Expense Tracker",
        ),
    ),
    # Swagger UI endpoint
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # ReDoc UI endpoint
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
