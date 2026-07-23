from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .filters import MaintenanceFilter
from .models import Maintenance


@login_required
def maintenance_list(request):
    user = request.user

    if user.groups.filter(name="Manager").exists() or user.is_superuser:
        maintenances = Maintenance.objects.all()

    elif user.groups.filter(name="Client").exists():
        maintenances = Maintenance.objects.filter(
            machine__client=user
        )

    elif user.groups.filter(name="Service").exists():
        maintenances = Maintenance.objects.filter(
            machine__service_company=user
        )

    else:
        maintenances = Maintenance.objects.none()


    maintenance_filter = MaintenanceFilter(
        request.GET,
        queryset=maintenances
    )


    maintenances = maintenance_filter.qs


    # Сортировка
    ordering = request.GET.get("ordering")

    if ordering:
        maintenances = maintenances.order_by(ordering)


    return render(
        request,
        "maintenance/maintenance_list.html",
        {
            "filter": maintenance_filter,
            "maintenances": maintenances,
            "ordering": ordering,
        },
    )



@login_required
def maintenance_detail(request, pk):
    user = request.user

    if user.groups.filter(name="Manager").exists() or user.is_superuser:
        maintenance = get_object_or_404(
            Maintenance,
            pk=pk
        )

    elif user.groups.filter(name="Client").exists():
        maintenance = get_object_or_404(
            Maintenance,
            pk=pk,
            machine__client=user
        )

    elif user.groups.filter(name="Service").exists():
        maintenance = get_object_or_404(
            Maintenance,
            pk=pk,
            machine__service_company=user
        )

    else:
        maintenance = get_object_or_404(
            Maintenance.objects.none(),
            pk=pk
        )


    return render(
        request,
        "maintenance/maintenance_detail.html",
        {
            "maintenance": maintenance,
        },
    )