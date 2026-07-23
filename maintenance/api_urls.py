from django.urls import path

from .api import MaintenanceAPIView


urlpatterns = [
    path("", MaintenanceAPIView.as_view(), name="api_maintenance"),
]