from django.urls import path

from .views import complaint_list, complaint_detail


app_name = "complaints"


urlpatterns = [
    path(
        "",
        complaint_list,
        name="complaint_list"
    ),

    path(
        "<int:pk>/",
        complaint_detail,
        name="complaint_detail"
    ),
]