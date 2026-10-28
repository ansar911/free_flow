from django.contrib import admin
from .models import ActivityLog


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):

    list_display = (
        "created_at",
        "user",
        "action",
    )

    list_filter = (
        "action",
        "created_at",
    )

    search_fields = (
        "description",
        "user__username",
    )

    ordering = (
        "-created_at",
    )