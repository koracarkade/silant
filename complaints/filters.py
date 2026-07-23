import django_filters

from .models import Complaint


class ComplaintFilter(django_filters.FilterSet):

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


    class Meta:
        model = Complaint

        fields = [
            "machine",
            "service_company",
        ]