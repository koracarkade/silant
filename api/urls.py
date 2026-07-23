from django.urls import path

from .views import (
    MachineAPIView,
    MaintenanceAPIView,
    ComplaintAPIView,
)


urlpatterns = [
    path(
        "machines/",
        MachineAPIView.as_view(),
        name="api_machines",
    ),

    path(
        "maintenance/",
        MaintenanceAPIView.as_view(),
        name="api_maintenance",
    ),

    path(
        "complaints/",
        ComplaintAPIView.as_view(),
        name="api_complaints",
    ),
]