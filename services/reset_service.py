from students.models import Student
from parents.models import Parent

from billing.models import (
    BillingCycle,
    Invoice,
    InvoiceItem,
)

from payments.models import (
    PaymentTransaction,
    PaymentAllocation,
)

from whatsapp.models import WhatsAppMessage


class ResetService:

    @staticmethod
    def reset_demo_data():

        WhatsAppMessage.objects.all().delete()

        PaymentAllocation.objects.all().delete()

        PaymentTransaction.objects.all().delete()

        InvoiceItem.objects.all().delete()

        Invoice.objects.all().delete()

        BillingCycle.objects.all().delete()

        Student.objects.all().delete()

        Parent.objects.all().delete()