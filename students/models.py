from django.db import models
from django.db.models import Max
from parents.models import Parent


class Student(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("ON_HOLD", "On Hold"),
        ("LEFT", "Left"),
    ]

    student_id = models.CharField(
        max_length=10,
        unique=True,
        editable=False,
    )

    name = models.CharField(max_length=100)

    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name="students",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE",
    )

    joined_date = models.DateField()

    def save(self, *args, **kwargs):

        if not self.student_id:

            last_student = Student.objects.aggregate(
                Max("student_id")
            )["student_id__max"]

            if last_student:
                number = int(last_student[2:]) + 1
            else:
                number = 1

            self.student_id = f"ST{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_id} - {self.name}"