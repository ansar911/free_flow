from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "name",
            "parent",
            "joined_date",
            "status",
        ]

        widgets = {
            "joined_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }