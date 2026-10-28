from django.contrib import admin
from .models import AcademySettings


@admin.register(AcademySettings)
class AcademySettingsAdmin(admin.ModelAdmin):

    list_display = (
        "academy_name",
        "monthly_fee",
        "upi_id",
        "whatsapp_number",
        "updated_at",
    )

    readonly_fields = (
        "updated_at",
    )