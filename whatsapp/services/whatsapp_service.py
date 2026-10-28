from billing.models import Invoice
from whatsapp.models import WhatsAppMessage
from .message_builder import MessageBuilder


class WhatsAppService:

    @staticmethod
    def queue_pending_messages():

        invoices = Invoice.objects.filter(
            status__in=["PENDING", "PARTIAL"]
        ).select_related(
            "parent",
            "billing_cycle",
        )

        count = 0

        for invoice in invoices:

            already_queued = WhatsAppMessage.objects.filter(
                invoice=invoice,
                status="PENDING",
            ).exists()

            if already_queued:
                continue

            message = MessageBuilder.build(invoice)

            WhatsAppMessage.objects.create(
                invoice=invoice,
                phone=invoice.parent.phone,
                message=message,
                status="PENDING",
            )

            count += 1

        return count