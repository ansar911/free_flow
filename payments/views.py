from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from billing.models import Invoice

from .forms import CashPaymentForm
from .services.payment_service import PaymentService
from .services.verification_service import VerificationService
from django.shortcuts import get_object_or_404
from payments.models import PaymentTransaction

@login_required
def invoice_list(request):

    from django.db.models import Q

    search = request.GET.get("search", "")

    invoices = Invoice.objects.select_related(
        "parent",
        "billing_cycle",
    ).filter(
        Q(parent__name__icontains=search) |
        Q(parent__phone__icontains=search) |
        Q(items__student__student_id__icontains=search) |
        Q(items__student__name__icontains=search)
    ).distinct().order_by("-created_at")

    return render(
        request,
        "payments/invoice_list.html",
        {
            "invoices": invoices,
        },
    )


@login_required
def receive_payment(request, invoice_id):

    invoice = get_object_or_404(
        Invoice,
        pk=invoice_id,
    )

    if request.method == "POST":

        form = CashPaymentForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            PaymentService.record_payment(

                invoice=invoice,

                amount=form.cleaned_data["amount"],

                payment_method=form.cleaned_data["payment_method"],

                transaction_id=form.cleaned_data["transaction_id"],

                screenshot=form.cleaned_data["screenshot"],

                notes=form.cleaned_data["notes"],

                user=request.user,

            )

            messages.success(
                request,
                "Payment recorded successfully."
            )

            return redirect("invoice_list")

    else:

        form = CashPaymentForm()

    balance = invoice.total_amount - invoice.paid_amount

    return render(
        request,
        "payments/receive_payment.html",
        {
            "invoice": invoice,
            "form": form,
            "balance": balance,
        },
    )

@login_required
def pending_payments(request):

    payments = PaymentTransaction.objects.filter(
        status="PENDING"
    ).order_by("-payment_date")

    return render(
        request,
        "payments/pending.html",
        {
            "payments": payments,
        },
    )


@login_required
def verify_payment(request, payment_id):

    payment = get_object_or_404(
        PaymentTransaction,
        pk=payment_id,
    )

    VerificationService.verify(
        payment,
        request.user,
    )

    messages.success(
        request,
        "Payment verified successfully."
    )

    return redirect(
        "pending_payments"
    )