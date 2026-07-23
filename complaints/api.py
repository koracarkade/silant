from rest_framework.generics import ListAPIView

from .models import Complaint
from .serializers import ComplaintSerializer


class ComplaintAPIView(ListAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer