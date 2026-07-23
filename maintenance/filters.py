import django_filters

from .models import Maintenance


class MaintenanceFilter(django_filters.FilterSet):

    machine = django_filters.CharFilter(
        field_name="machine__factory_number",
        lookup_expr="icontains",
        label="Заводской номер машины"
    )

    service_company = django_filters.CharFilter(
        field_name="machine__service_company__username",
        lookup_expr="icontains",
        label="Сервисная компания"
    )

    maintenance_type = django_filters.CharFilter(
        method="filter_maintenance_type",
        label="Вид ТО"
    )

    def filter_maintenance_type(self, queryset, name, value):
        return queryset.filter(
            maintenance_type__name__icontains=value,
            maintenance_type__entity_name="maintenance_type"
        )

    class Meta:
        model = Maintenance

        fields = [
            "machine",
            "service_company",
            "maintenance_type",
        ]