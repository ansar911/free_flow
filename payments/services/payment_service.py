from decimal import Decimal

from django.db import transaction

from billing.models import InvoiceItem
from payments.models import PaymentTransaction, PaymentAllocation
from whatsapp.services.queue_service import QueueService
from logs.services.logger import Logger


class PaymentService:

    @staticmethod
    @transaction.atomic
    def record_payment(
        invoice,
        amount,
        payment_method,
        transaction_id="",
        screenshot=None,
        notes="",
        user=None,
    ):

        payment = PaymentTransaction.objects.create(
            invoice=invoice,
            amount=amount,
            payment_method=payment_method,
            transaction_id=transaction_id,
            screenshot=screenshot,
            notes=notes,
        )

        remaining = Decimal(str(amount))

        items = invoice.items.filter(
            status="PENDING"
        ).order_by("id")

        for item in items:

            if remaining <= 0:
                break

            pay_amount = min(remaining, item.amount)

            PaymentAllocation.objects.create(
                transaction=payment,
                invoice_item=item,
                amount=pay_amount,
            )

            if pay_amount == item.amount:
                item.status = "PAID"
                item.save()

            remaining -= pay_amount

        total_paid = sum(
            t.amount for t in invoice.transactions.all()
        )

        invoice.paid_amount = total_paid

        if invoice.paid_amount == 0:
            invoice.status = "PENDING"

        elif invoice.paid_amount < invoice.total_amount:
            invoice.status = "PARTIAL"

        else:
            invoice.status = "PAID"

            invoice.save()

            if invoice.status == "PAID":

                QueueService.cancel_invoice_queue(invoice)
                if user:

                    Logger.log(
                        user,
                        "PAYMENT",
                        (
                            f"Received ₹{amount} from "
                            f"{invoice.parent.name} "
                            f"for {invoice.billing_cycle.name}"
                        ),
                    )
            return payment