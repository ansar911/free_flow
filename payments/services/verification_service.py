from django.db import transaction

from logs.services.logger import Logger


class VerificationService:

    @staticmethod
    @transaction.atomic
    def verify(payment, user):

        if payment.status == "VERIFIED":
            return

        payment.status = "VERIFIED"
        payment.verified_by = user.username
        payment.save()

        invoice = payment.invoice

        invoice.paid_amount = sum(
            t.amount
            for t in invoice.transactions.filter(
                status="VERIFIED"
            )
        )

        if invoice.paid_amount == 0:

            invoice.status = "PENDING"

        elif invoice.paid_amount < invoice.total_amount:

            invoice.status = "PARTIAL"

        else:

            invoice.status = "PAID"

            for item in invoice.items.all():

                item.status = "PAID"
                item.save()

            from whatsapp.services.queue_service import QueueService

            QueueService.cancel_invoice_queue(invoice)

        invoice.save()

        Logger.log(
            user,
            "VERIFY_PAYMENT",
            (
                f"Verified payment from "
                f"{invoice.parent.name}"
            ),
        )