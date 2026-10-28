from whatsapp.models import WhatsAppMessage


class QueueService:

    @staticmethod
    def cancel_invoice_queue(invoice):

        WhatsAppMessage.objects.filter(
            invoice=invoice,
            status="PENDING",
        ).update(
            status="CANCELLED",
        )