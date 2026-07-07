from django.contrib import admin
from .models import Parent

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone")
    search_fields = ("name", "phone")