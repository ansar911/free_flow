from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from settings_app.models import AcademySettings

from .models import Invoice
from .forms import (
    BillingGenerationForm,
    ParentPaymentForm,
)

from .services.billing_preview import BillingPreview
from .services.billing_generator import BillingGenerator



@login_required
def billing_dashboard(request):

    preview = None
    result = None

    form = BillingGenerationForm()

    if request.method == "POST":

        action = request.POST.get("action")

        form = BillingGenerationForm(request.POST)

        if form.is_valid():

            month = int(form.cleaned_data["month"])
            year = form.cleaned_data["year"]

            if action == "preview":

                preview = BillingPreview.get(
                    month,
                    year,
                )

            elif action == "generate":

                try:

                    result = BillingGenerator.generate(
                        month,
                        year,
                        request.user,
                    )

                    messages.success(
                        request,
                        "Billing generated successfully."
                    )

                except Exception as e:

                    messages.error(
                        request,
                        str(e),
                    )

    return render(
        request,
        "billing/dashboard.html",
        {
            "form": form,
            "preview": preview,
            "result": result,
        },
    )


def parent_payment(request, token):

    invoice = get_object_or_404(
        Invoice,
        payment_token=token,
    )

    # Invoice already paid
    if invoice.status == "PAID":

        return render(
            request,
            "billing/payment_complete.html",
            {
                "invoice": invoice,
            },
        )

    # Payment waiting for verification
    existing_payment = invoice.transactions.filter(
        status="PENDING"
    ).first()

    if existing_payment:

        return render(
            request,
            "billing/payment_pending.html",
            {
                "invoice": invoice,
            },
        )

    settings = AcademySettings.objects.first()

    form = ParentPaymentForm()

    return render(
        request,
        "billing/parent_payment.html",
        {
            "invoice": invoice,
            "settings": settings,
            "form": form,
        },
    )

def submit_payment(request, token):

    invoice = get_object_or_404(
        Invoice,
        payment_token=token,
    )

    # Prevent duplicate submissions
    existing_payment = invoice.transactions.filter(
        status="PENDING"
    ).exists()

    if existing_payment:

        return redirect(
            "parent_payment",
            token=token,
        )

    if request.method != "POST":

        return redirect(
            "parent_payment",
            token=token,
        )

    form = ParentPaymentForm(
        request.POST,
        request.FILES,
    )

    if form.is_valid():

        payment = form.save(commit=False)

        payment.invoice = invoice

        payment.amount = (
            invoice.total_amount
            - invoice.paid_amount
        )

        payment.status = "PENDING"

        payment.save()

        return render(
            request,
            "billing/payment_success.html",
            {
                "invoice": invoice,
            },
        )

    settings = AcademySettings.objects.first()

    return render(
        request,
        "billing/parent_payment.html",
        {
            "invoice": invoice,
            "settings": settings,
            "form": form,
        },
    )


@login_required
def generate_billing(request):

    return billing_dashboard(request)