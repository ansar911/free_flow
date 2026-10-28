from django import forms


class WhatsAppTestForm(forms.Form):

    phone = forms.CharField(

        max_length=20,

        label="Test Phone Number",

        help_text="Example: 919876543210",

        widget=forms.TextInput(

            attrs={

                "class": "form-control",

                "placeholder": "919876543210",

            }

        ),

    )