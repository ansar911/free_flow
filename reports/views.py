from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from students.models import Student
from billing.models import Invoice


@login_required
def report_dashboard(request):

    total_students = Student.objects.count()

    paid = Invoice.objects.filter(status="PAID").count()

    partial = Invoice.objects.filter(status="PARTIAL").count()

    pending = Invoice.objects.filter(status="PENDING").count()

    collected = sum(
        invoice.paid_amount
        for invoice in Invoice.objects.all()
    )

    expected = sum(
        invoice.total_amount
        for invoice in Invoice.objects.all()
    )

    return render(
        request,
        "reports/dashboard.html",
        {
            "total_students": total_students,
            "paid": paid,
            "partial": partial,
            "pending": pending,
            "collected": collected,
            "expected": expected,
        },
    )