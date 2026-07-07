from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from parents.models import Parent
from students.models import Student
from payments.models import Payment


@login_required
def dashboard(request):

    total_students = Student.objects.filter(status="ACTIVE").count()

    total_parents = Parent.objects.count()

    pending_payments = Payment.objects.filter(
        status="Pending"
    ).count()

    collected = sum(
        payment.amount
        for payment in Payment.objects.filter(status="Paid")
    )

    context = {

        "total_students": total_students,

        "total_parents": total_parents,

        "pending_payments": pending_payments,

        "collected": collected,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )