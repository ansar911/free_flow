from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLES = [
        ("OWNER", "Owner"),
        ("ADMIN", "Admin"),
        ("ACCOUNTANT", "Accountant"),
        ("STAFF", "Staff"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default="STAFF",
    )

    def __str__(self):
        return f"{self.user.username} ({self.role})"