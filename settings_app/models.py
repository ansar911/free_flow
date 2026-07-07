from django.db import models


class AcademySettings(models.Model):
    academy_name = models.CharField(max_length=100)
    monthly_fee = models.DecimalField(max_digits=8, decimal_places=2)

    upi_id = models.CharField(max_length=100)

    qr_code = models.ImageField(
        upload_to="qr_codes/"
    )

    whatsapp_number = models.CharField(max_length=15)

    def __str__(self):
        return self.academy_name