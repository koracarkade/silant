from django.contrib import admin

from .models import Machine


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = (
        "factory_number",
        "machine_model",
        "engine_model",
        "shipment_date",
        "client",
        "service_company",
    )

    list_filter = (
        "machine_model",
        "engine_model",
        "transmission_model",
        "drive_axle_model",
        "steering_axle_model",
        "service_company",
    )

    search_fields = (
        "factory_number",
        "engine_number",
        "transmission_number",
        "drive_axle_number",
        "steering_axle_number",
        "consignee",
    )

    ordering = (
        "shipment_date",
    )