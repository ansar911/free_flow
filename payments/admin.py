from django.contrib import admin

from .models import PaymentTransaction, PaymentAllocation


@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):

    list_display = (
        "invoice",
        "amount",
        "payment_method",
        "status",
        "payment_date",
    )

    list_filter = (
        "status",
        "payment_method",
    )

    search_fields = (
        "transaction_id",
        "invoice__parent__name",
    )


@admin.register(PaymentAllocation)
class PaymentAllocationAdmin(admin.ModelAdmin):

    list_display = (
        "transaction",
        "invoice_item",
        "amount",
    )