from rest_framework.generics import ListAPIView

from .models import Maintenance
from .serializers import MaintenanceSerializer


class MaintenanceAPIView(ListAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer