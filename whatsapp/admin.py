from django.contrib import admin
from .models import WhatsAppMessage


@admin.register(WhatsAppMessage)
class WhatsAppMessageAdmin(admin.ModelAdmin):

    list_display = (
        "phone",
        "status",
        "created_at",
        "sent_at",
    )

    list_filter = (
        "status",
    )