from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .filters import ComplaintFilter
from .models import Complaint


@login_required
def complaint_list(request):
    user = request.user

    if user.groups.filter(name="Manager").exists() or user.is_superuser:
        complaints = Complaint.objects.all()

    elif user.groups.filter(name="Client").exists():
        complaints = Complaint.objects.filter(
            machine__client=user
        )

    elif user.groups.filter(name="Service").exists():
        complaints = Complaint.objects.filter(
            machine__service_company=user
        )

    else:
        complaints = Complaint.objects.none()


    complaint_filter = ComplaintFilter(
        request.GET,
        queryset=complaints
    )


    return render(
        request,
        "complaints/complaint_list.html",
        {
            "filter": complaint_filter,
            "complaints": complaint_filter.qs,
        },
    )


@login_required
def complaint_detail(request, pk):
    user = request.user

    if user.groups.filter(name="Manager").exists() or user.is_superuser:
        complaint = get_object_or_404(
            Complaint,
            pk=pk
        )

    elif user.groups.filter(name="Client").exists():
        complaint = get_object_or_404(
            Complaint,
            pk=pk,
            machine__client=user
        )

    elif user.groups.filter(name="Service").exists():
        complaint = get_object_or_404(
            Complaint,
            pk=pk,
            machine__service_company=user
        )

    else:
        complaint = get_object_or_404(
            Complaint.objects.none(),
            pk=pk
        )


    return render(
        request,
        "complaints/complaint_detail.html",
        {
            "complaint": complaint,
        },
    )