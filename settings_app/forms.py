from django import forms

from .models import AcademySettings


class AcademySettingsForm(forms.ModelForm):

    class Meta:

        model = AcademySettings

        fields = [

            # Academy
            "academy_name",
            "academy_phone",
            "academy_email",
            "address",

            # Fee Settings
            "monthly_fee",
            "late_fee",
            "reminder_day",

            # Payment
            "upi_id",
            "gpay_number",
            "qr_code",

            # WhatsApp
            "whatsapp_number",
            "whatsapp_provider",
            "whatsapp_enabled",
            "whatsapp_business_account_id",
            "whatsapp_phone_number_id",
            "whatsapp_access_token",
            "whatsapp_api_version",
            "whatsapp_template_name",

        ]

        widgets = {

            "academy_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "academy_phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "academy_email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "monthly_fee": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "late_fee": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "reminder_day": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "upi_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "gpay_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "qr_code": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "whatsapp_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "whatsapp_provider": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "whatsapp_enabled": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "whatsapp_business_account_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "whatsapp_phone_number_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "whatsapp_access_token": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),

            "whatsapp_api_version": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "whatsapp_template_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

        }