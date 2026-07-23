from django.urls import path

from .api import ComplaintAPIView


urlpatterns = [
    path("", ComplaintAPIView.as_view(), name="api_complaints"),
]