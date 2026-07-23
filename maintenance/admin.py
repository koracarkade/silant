from django.contrib import admin

from .models import Maintenance


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        "machine",
        "maintenance_date",
        "employee",
    )

    list_filter = (
        "maintenance_date",
    )

    search_fields = (
        "machine__serial_number",
        "employee",
    )