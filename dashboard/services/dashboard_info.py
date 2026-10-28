from decimal import Decimal

from students.models import Student
from parents.models import Parent

from billing.models import Invoice

from payments.models import PaymentTransaction

from whatsapp.models import WhatsAppMessage

from logs.models import ActivityLog


class DashboardService:

    @staticmethod
    def get_dashboard():

        total_students = Student.objects.count()

        active_students = Student.objects.filter(
            status="ACTIVE"
        ).count()

        total_parents = Parent.objects.count()

        total_invoices = Invoice.objects.count()

        paid_invoices = Invoice.objects.filter(
            status="PAID"
        ).count()

        partial_invoices = Invoice.objects.filter(
            status="PARTIAL"
        ).count()

        pending_invoices = Invoice.objects.filter(
            status="PENDING"
        ).count()

        total_expected = Decimal("0.00")

        total_collected = Decimal("0.00")

        for invoice in Invoice.objects.all():

            total_expected += invoice.total_amount

            total_collected += invoice.paid_amount

        if total_expected > 0:

            collection_percent = round(
                (total_collected / total_expected) * 100,
                1,
            )

        else:

            collection_percent = 0

        pending_verification = PaymentTransaction.objects.filter(
            status="PENDING",
        ).count()

        whatsapp_pending = WhatsAppMessage.objects.filter(
            status="PENDING",
        ).count()

        whatsapp_failed = WhatsAppMessage.objects.filter(
            status="FAILED",
        ).count()

        recent_logs = ActivityLog.objects.select_related(
            "user",
        )[:10]

        return {

            "total_students": total_students,

            "active_students": active_students,

            "total_parents": total_parents,

            "total_invoices": total_invoices,

            "paid_invoices": paid_invoices,

            "partial_invoices": partial_invoices,

            "pending_invoices": pending_invoices,

            "total_expected": total_expected,

            "total_collected": total_collected,

            "collection_percent": collection_percent,

            "pending_verification": pending_verification,

            "whatsapp_pending": whatsapp_pending,

            "whatsapp_failed": whatsapp_failed,

            "recent_logs": recent_logs,

        }