from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "accounts/",
        include("allauth.urls")
    ),

    path(
        "",
        include("machines.urls")
    ),

    path(
        "maintenance/",
        include("maintenance.urls")
    ),

    path(
        "complaints/",
        include("complaints.urls")
    ),

    path(
        "api/",
        include("api.urls")
    ),
]