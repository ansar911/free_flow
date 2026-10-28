from django.db import models


class AcademySettings(models.Model):

    academy_name = models.CharField(
        max_length=200,
        default="Indian Fitness",
    )

    monthly_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1000,
    )

    upi_id = models.CharField(
        max_length=100,
        blank=True,
    )

    gpay_number = models.CharField(
        max_length=15,
        blank=True,
    )

    whatsapp_number = models.CharField(
        max_length=15,
        blank=True,
    )

    reminder_day = models.PositiveSmallIntegerField(
        default=5,
    )

    late_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    academy_phone = models.CharField(
        max_length=15,
        blank=True,
    )

    academy_email = models.EmailField(
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    qr_code = models.ImageField(
        upload_to="qr_codes/",
        blank=True,
        null=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Academy Settings"
        verbose_name_plural = "Academy Settings"

    whatsapp_enabled = models.BooleanField(
    default=False,
    )

    WHATSAPP_PROVIDERS = [

        ("META", "Meta WhatsApp Cloud API"),

        ("TWILIO", "Twilio"),

        ("DISABLED", "Disabled"),

    ]

    whatsapp_provider = models.CharField(

        max_length=30,

        choices=WHATSAPP_PROVIDERS,

        default="META",

    )

    whatsapp_phone_number_id = models.CharField(
        max_length=100,
        blank=True,
    )

    whatsapp_business_account_id = models.CharField(
        max_length=100,
        blank=True,
    )

    whatsapp_access_token = models.TextField(
        blank=True,
    )

    whatsapp_api_version = models.CharField(
        max_length=20,
        default="v23.0",
    )

    whatsapp_template_name = models.CharField(
        max_length=100,
        default="monthly_fee",
    )

    country_code = models.CharField(
        max_length=5,
        default="+91",
    )    

    def __str__(self):
        return self.academy_name