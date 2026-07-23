from rest_framework import generics

from machines.models import Machine
from maintenance.models import Maintenance
from complaints.models import Complaint

from .serializers import (
    MachineSerializer,
    MaintenanceSerializer,
    ComplaintSerializer,
)


class MachineAPIView(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class MaintenanceAPIView(generics.ListAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ComplaintAPIView(generics.ListAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer