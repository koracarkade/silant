from django.contrib.auth.models import User
from django.db import models

from references.models import Reference


class Machine(models.Model):
    """Модель машины."""

    factory_number = models.CharField(
        "Заводской номер машины",
        max_length=100,
        unique=True,
    )

    machine_model = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        related_name="machine_models",
        limit_choices_to={"entity_name": "machine_model"},
        verbose_name="Модель техники",
    )

    engine_model = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        related_name="engine_models",
        limit_choices_to={"entity_name": "engine_model"},
        verbose_name="Модель двигателя",
    )

    engine_number = models.CharField(
        "Заводской номер двигателя",
        max_length=100,
    )

    transmission_model = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        related_name="transmission_models",
        limit_choices_to={"entity_name": "transmission_model"},
        verbose_name="Модель трансмиссии",
    )

    transmission_number = models.CharField(
        "Заводской номер трансмиссии",
        max_length=100,
    )

    drive_axle_model = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        related_name="drive_axle_models",
        limit_choices_to={"entity_name": "drive_axle_model"},
        verbose_name="Модель ведущего моста",
    )

    drive_axle_number = models.CharField(
        "Заводской номер ведущего моста",
        max_length=100,
    )

    steering_axle_model = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        related_name="steering_axle_models",
        limit_choices_to={"entity_name": "steering_axle_model"},
        verbose_name="Модель управляемого моста",
    )

    steering_axle_number = models.CharField(
        "Заводской номер управляемого моста",
        max_length=100,
    )

    supply_contract = models.CharField(
        "Договор поставки",
        max_length=255,
    )

    shipment_date = models.DateField(
        "Дата отгрузки с завода",
    )

    buyer = models.CharField(
        "Покупатель",
        max_length=255,
    )

    consignee = models.CharField(
        "Грузополучатель",
        max_length=255,
    )

    delivery_address = models.CharField(
        "Адрес поставки",
        max_length=255,
    )

    equipment = models.TextField(
        "Комплектация",
        blank=True,
    )

    client = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="client_machines",
        verbose_name="Клиент",
    )

    service_company = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="service_company_machines",
        verbose_name="Сервисная компания",
    )

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
        ordering = ["shipment_date"]

    def __str__(self):
        return self.factory_number