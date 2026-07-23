import django_filters

from .models import Machine


class MachineFilter(django_filters.FilterSet):

    factory_number = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Заводской номер"
    )

    machine_model = django_filters.CharFilter(
        field_name="machine_model__name",
        lookup_expr="icontains",
        label="Модель техники"
    )

    engine_model = django_filters.CharFilter(
        field_name="engine_model__name",
        lookup_expr="icontains",
        label="Модель двигателя"
    )

    transmission_model = django_filters.CharFilter(
        field_name="transmission_model__name",
        lookup_expr="icontains",
        label="Модель трансмиссии"
    )

    drive_axle_model = django_filters.CharFilter(
        field_name="drive_axle_model__name",
        lookup_expr="icontains",
        label="Модель ведущего моста"
    )

    steering_axle_model = django_filters.CharFilter(
        field_name="steering_axle_model__name",
        lookup_expr="icontains",
        label="Модель управляемого моста"
    )

    class Meta:
        model = Machine

        fields = [
            "factory_number",
            "machine_model",
            "engine_model",
            "transmission_model",
            "drive_axle_model",
            "steering_axle_model",
        ]