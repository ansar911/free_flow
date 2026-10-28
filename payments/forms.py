from django import forms


class CashPaymentForm(forms.Form):

    amount = forms.DecimalField(
        min_value=1,
        decimal_places=2,
    )

    PAYMENT_METHODS = [
        ("CASH", "Cash"),
        ("UPI", "UPI"),
    ]

    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHODS,
    )

    transaction_id = forms.CharField(
        required=False,
    )

    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
    )

    screenshot = forms.ImageField(
        required=False,
    )