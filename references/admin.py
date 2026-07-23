from django.contrib import admin

from .models import Reference


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "entity_name",
    )

    list_filter = (
        "entity_name",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "entity_name",
        "name",
    )