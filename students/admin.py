from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "student_id",
        "name",
        "parent",
        "status",
        "joined_date",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "student_id",
        "name",
        "parent__name",
        "parent__phone",
    )

    ordering = (
        "student_id",
    )