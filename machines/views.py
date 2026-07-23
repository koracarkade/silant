from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .filters import MachineFilter
from .models import Machine


@login_required
def machine_list(request):
    user = request.user

    if user.groups.filter(name="Manager").exists() or user.is_superuser:
        machines = Machine.objects.all()

    elif user.groups.filter(name="Client").exists():
        machines = Machine.objects.filter(client=user)

    elif user.groups.filter(name="Service").exists():
        machines = Machine.objects.filter(service_company=user)

    else:
        machines = Machine.objects.none()


    machine_filter = MachineFilter(
        request.GET,
        queryset=machines
    )


    machines = machine_filter.qs


    # Сортировка
    ordering = request.GET.get("ordering")

    if ordering:
        machines = machines.order_by(ordering)


    return render(
        request,
        "machines/machine_list.html",
        {
            "filter": machine_filter,
            "machines": machines,
            "ordering": ordering,
        },
    )


@login_required
def machine_detail(request, pk):
    machine = get_object_or_404(
        Machine,
        pk=pk
    )


    if (
        request.user.is_superuser
        or request.user.groups.filter(name="Manager").exists()
        or machine.client == request.user
        or machine.service_company == request.user
    ):
        return render(
            request,
            "machines/machine_detail.html",
            {
                "machine": machine,
            },
        )


    return render(
        request,
        "403.html",
        status=403
    )