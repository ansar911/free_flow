from collections import defaultdict
from decimal import Decimal
import calendar

from django.db import transaction

from students.models import Student
from settings_app.models import AcademySettings

from billing.models import BillingCycle, Invoice, InvoiceItem

from logs.services.logger import Logger

class BillingGenerator:

    @staticmethod
    @transaction.atomic
    def generate(month, year, user=None):

        settings = AcademySettings.objects.first()

        if not settings:
            raise Exception("Academy Settings not configured.")

        cycle_name = f"{calendar.month_name[month]} {year}"

        billing_cycle, created = BillingCycle.objects.get_or_create(
            month=month,
            year=year,
            defaults={
                "name": cycle_name,
            },
        )

        if not created:
            raise Exception(
                f"Billing already exists for {cycle_name}"
            )

        from datetime import date

        last_day = calendar.monthrange(year, month)[1]

        billing_date = date(
            year,
            month,
            last_day,
        )

        students = Student.objects.filter(
            status="ACTIVE",
            joined_date__lte=billing_date,
        ).select_related("parent")

        grouped = defaultdict(list)

        for student in students:
            grouped[student.parent].append(student)

        invoice_count = 0
        student_count = 0
        expected_income = Decimal("0.00")

        for parent, children in grouped.items():

            invoice = Invoice.objects.create(
                billing_cycle=billing_cycle,
                parent=parent,
            )

            total = Decimal("0.00")

            for child in children:

                InvoiceItem.objects.create(
                    invoice=invoice,
                    student=child,
                    amount=settings.monthly_fee,
                )

                total += settings.monthly_fee
                student_count += 1

            invoice.total_amount = total
            invoice.save()

            expected_income += total
            invoice_count += 1
        if user:

            Logger.log(
                user,
                "GENERATE_BILLING",
                (
                    f"Generated billing for {cycle_name} | "
                    f"Invoices: {invoice_count} | "
                    f"Students: {student_count} | "
                    f"Expected Income: ₹{expected_income}"
                ),
            )
        return {
            "billing_cycle": billing_cycle,
            "invoice_count": invoice_count,
            "student_count": student_count,
            "expected_income": expected_income,
        }