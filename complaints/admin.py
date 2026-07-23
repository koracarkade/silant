from django.contrib import admin

from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "machine",
        "complaint_date",
        "status",
    )

    list_filter = (
        "status",
        "complaint_date",
    )

    search_fields = (
        "machine__serial_number",
        "description",
    )