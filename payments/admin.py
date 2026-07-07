from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "month",
        "year",
        "amount",
        "status",
        "payment_method",
        "paid_date",
    )

    list_filter = (
        "status",
        "payment_method",
        "month",
        "year",
    )

    search_fields = (
        "student__name",
        "student__student_id",
    )