import uuid

from django.db import models

from parents.models import Parent
from students.models import Student



class BillingCycle(models.Model):

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("LOCKED", "Locked"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=30,
        unique=True,
    )

    month = models.PositiveSmallIntegerField()

    year = models.PositiveSmallIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-year", "-month"]

    def __str__(self):
        return self.name


class Invoice(models.Model):
    payment_token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )


    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PARTIAL", "Partial"),
        ("PAID", "Paid"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    billing_cycle = models.ForeignKey(
        BillingCycle,
        on_delete=models.CASCADE,
        related_name="invoices",
    )

    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name="invoices",
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = (
            "billing_cycle",
            "parent",
        )

    def __str__(self):
        return f"{self.parent.name} - {self.billing_cycle.name}"


class InvoiceItem(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
    ]

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="items",
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    class Meta:
        unique_together = (
            "invoice",
            "student",
        )

    def __str__(self):
        return self.student.name