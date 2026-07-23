from django.urls import path

from .api import MachineAPIView
from .views import machine_detail, machine_list


app_name = "machines"


urlpatterns = [
    path("", machine_list, name="machine_list"),

    path(
        "machine/<int:pk>/",
        machine_detail,
        name="machine_detail",
    ),

    path(
        "api/machines/",
        MachineAPIView.as_view(),
        name="api_machines",
    ),
]