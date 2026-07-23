from django.db import models

from machines.models import Machine


class Complaint(models.Model):
    STATUS_CHOICES = [
        ("new", "Новая"),
        ("in_progress", "В работе"),
        ("closed", "Закрыта"),
    ]

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="complaints",
        verbose_name="Машина"
    )

    complaint_date = models.DateField(
        verbose_name="Дата рекламации"
    )

    description = models.TextField(
        verbose_name="Описание проблемы"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
        verbose_name="Статус"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )


    class Meta:
        verbose_name = "Рекламация"
        verbose_name_plural = "Рекламации"
        ordering = ["-complaint_date"]


    def __str__(self):
        return f"Рекламация {self.machine} от {self.complaint_date}"