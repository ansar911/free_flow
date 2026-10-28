from django.db import models
from django.contrib.auth.models import User


class ActivityLog(models.Model):

    ACTIONS = [

        ("LOGIN", "Login"),
        ("ADD_STUDENT", "Add Student"),
        ("EDIT_STUDENT", "Edit Student"),
        ("ADD_PARENT", "Add Parent"),
        ("EDIT_PARENT", "Edit Parent"),
        ("GENERATE_BILLING", "Generate Billing"),
        ("PAYMENT", "Receive Payment"),
        ("VERIFY_PAYMENT", "Verify Payment"),
        ("SETTINGS", "Settings Updated"),
        ("RESET", "Reset Demo Data"),
        ("AUTO_BILLING", "Automatic Billing"),

    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    action = models.CharField(
        max_length=30,
        choices=ACTIONS,
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = [
            "-created_at",
        ]

    def __str__(self):

        return f"{self.action}"