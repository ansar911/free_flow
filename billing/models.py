import uuid

from django.db import models

from parents.models import Parent

from students.models import Student


class BillingCycle(models.Model):

    STATUS = [

        ("OPEN", "Open"),

        ("LOCKED", "Locked"),

    ]

    id = models.UUIDField(

        primary_key=True,

        default=uuid.uuid4,

        editable=False,

    )

    month = models.IntegerField()

    year = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(

        max_length=20,

        choices=STATUS,

        default="OPEN",

    )

    class Meta:

        unique_together = ("month", "year")

    def __str__(self):

        return f"{self.month}/{self.year}"


class Invoice(models.Model):

    id = models.UUIDField(

        primary_key=True,

        default=uuid.uuid4,

        editable=False,

    )

    billing_cycle = models.ForeignKey(

        BillingCycle,

        on_delete=models.CASCADE,

    )

    parent = models.ForeignKey(

        Parent,

        on_delete=models.CASCADE,

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

    created_at = models.DateTimeField(

        auto_now_add=True,

    )

    def __str__(self):

        return f"{self.parent.name}"
        

class InvoiceItem(models.Model):

    STATUS = [

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

        choices=STATUS,

        default="PENDING",

    )

    paid_date = models.DateField(

        null=True,

        blank=True,

    )

    payment_method = models.CharField(

        max_length=20,

        blank=True,

    )

    screenshot = models.ImageField(

        upload_to="payments/",

        null=True,

        blank=True,

    )

    def __str__(self):

        return self.student.name