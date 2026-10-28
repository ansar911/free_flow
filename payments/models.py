from django.db import models
from billing.models import Invoice, InvoiceItem


class PaymentTransaction(models.Model):

    PAYMENT_METHODS = [
        ("UPI", "UPI"),
        ("CASH", "Cash"),
        ("BANK", "Bank Transfer"),
    ]

    STATUS = [
        ("PENDING", "Pending"),
        ("VERIFIED", "Verified"),
        ("REJECTED", "Rejected"),
    ]

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
    )

    screenshot = models.ImageField(
        upload_to="media/payments/",
        blank=True,
        null=True,
    )

    payment_date = models.DateTimeField(
        auto_now_add=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="PENDING",
    )

    verified_by = models.CharField(
        max_length=100,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    def __str__(self):
        return f"{self.invoice.parent.name} - ₹{self.amount}"


class PaymentAllocation(models.Model):

    transaction = models.ForeignKey(
        PaymentTransaction,
        on_delete=models.CASCADE,
        related_name="allocations",
    )

    invoice_item = models.ForeignKey(
        InvoiceItem,
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return str(self.invoice_item)
