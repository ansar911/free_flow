from django.db import models
from students.models import Student


class Payment(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
    ]

    PAYMENT_METHODS = [
        ("UPI", "UPI"),
        ("Cash", "Cash"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    month = models.IntegerField()
    year = models.IntegerField()

    amount = models.DecimalField(max_digits=8, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        blank=True
    )

    screenshot = models.ImageField(
        upload_to="payments/",
        blank=True,
        null=True
    )

    paid_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "month", "year")

    def __str__(self):
        return f"{self.student.name} - {self.month}/{self.year}"