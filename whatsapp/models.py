from django.db import models
from billing.models import Invoice


class WhatsAppMessage(models.Model):

    STATUS = [
        ("PENDING", "Pending"),
        ("SENT", "Sent"),
        ("FAILED", "Failed"),
        ("CANCELLED", "Cancelled"),
]
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
    )

    phone = models.CharField(max_length=20)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="PENDING",
    )

    sent_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.phone