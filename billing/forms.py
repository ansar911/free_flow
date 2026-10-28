from django import forms
import calendar
from datetime import datetime

from payments.models import PaymentTransaction


class BillingGenerationForm(forms.Form):

    MONTHS = [
        (i, calendar.month_name[i])
        for i in range(1, 13)
    ]

    month = forms.ChoiceField(
        choices=MONTHS
    )

    year = forms.IntegerField(
        initial=datetime.now().year,
        min_value=2025,
        max_value=2100,
    )


class ParentPaymentForm(forms.ModelForm):

    class Meta:

        model = PaymentTransaction

        fields = [
            "payment_method",
            "transaction_id",
            "screenshot",
            "notes",
        ]

        widgets = {

            "payment_method": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "transaction_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "UPI Reference (Optional)",
                }
            ),

            "screenshot": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Remarks (Optional)",
                }
            ),

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["payment_method"].choices = [
            ("UPI", "UPI"),
        ]

    def clean(self):

        cleaned_data = super().clean()

        screenshot = cleaned_data.get("screenshot")

        if not screenshot:

            raise forms.ValidationError(
                "Please upload your payment screenshot."
            )

        return cleaned_data