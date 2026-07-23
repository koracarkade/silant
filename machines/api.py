from rest_framework.generics import ListAPIView

from .models import Machine
from .serializers import MachineSerializer


class MachineAPIView(ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer