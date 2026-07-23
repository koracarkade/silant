from django.db import models

from machines.models import Machine
from references.models import Reference


class Maintenance(models.Model):
    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="maintenances",
        verbose_name="Машина"
    )

    maintenance_type = models.ForeignKey(
        Reference,
        on_delete=models.PROTECT,
        related_name="maintenance_types",
        limit_choices_to={"entity_name": "maintenance_type"},
        verbose_name="Вид ТО",
    )

    maintenance_date = models.DateField(
        verbose_name="Дата проведения ТО"
    )

    description = models.TextField(
        verbose_name="Описание работ"
    )

    employee = models.CharField(
        max_length=150,
        verbose_name="Ответственный сотрудник"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания записи"
    )

    class Meta:
        verbose_name = "Техническое обслуживание"
        verbose_name_plural = "Технические обслуживания"
        ordering = ["maintenance_date"]

    def __str__(self):
        return f"ТО {self.machine} от {self.maintenance_date}"