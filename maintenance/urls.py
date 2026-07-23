from django.urls import path

from .api import MaintenanceAPIView
from .views import maintenance_detail, maintenance_list


app_name = "maintenance"


urlpatterns = [
    path("", maintenance_list, name="maintenance_list"),

    path(
        "maintenance/<int:pk>/",
        maintenance_detail,
        name="maintenance_detail",
    ),

    path(
        "api/maintenance/",
        MaintenanceAPIView.as_view(),
        name="api_maintenance",
    ),
]