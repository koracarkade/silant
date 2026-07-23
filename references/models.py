from django.db import models


class Reference(models.Model):
    ENTITY_CHOICES = [
        ("machine_model", "Модель техники"),
        ("engine_model", "Модель двигателя"),
        ("transmission_model", "Модель трансмиссии"),
        ("drive_axle_model", "Модель ведущего моста"),
        ("steering_axle_model", "Модель управляемого моста"),
        ("maintenance_type", "Вид ТО"),
        ("service_company", "Сервисная компания"),
        ("failure_node", "Узел отказа"),
        ("recovery_method", "Способ восстановления"),
        ("maintenance_company", "Организация, проводившая ТО"),
    ]

    entity_name = models.CharField(
        "Название сущности",
        max_length=50,
        choices=ENTITY_CHOICES,
    )

    name = models.CharField(
        "Название",
        max_length=255,
    )

    description = models.TextField(
        "Описание",
        blank=True,
    )

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"
        ordering = ("entity_name", "name")

    def __str__(self):
        return self.name