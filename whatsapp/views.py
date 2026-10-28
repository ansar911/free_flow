from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import WhatsAppMessage
from .services.whatsapp_service import WhatsAppService


@login_required
def whatsapp_dashboard(request):

    queue = (
        WhatsAppMessage.objects
        .select_related(
            "invoice",
            "invoice__parent",
            "invoice__billing_cycle",
        )
        .prefetch_related(
            "invoice__items__student",
        )
        .order_by("-created_at")
    )

    return render(
        request,
        "whatsapp/dashboard.html",
        {
            "queue": queue,
        },
    )


@login_required
def generate_queue(request):

    total = WhatsAppService.queue_pending_messages()

    messages.success(
        request,
        f"{total} messages added to queue."
    )

    return redirect("whatsapp_dashboard")

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import WhatsAppTestForm
from .services.meta_service import MetaWhatsAppService


@login_required
def test_connection(request):

    form = WhatsAppTestForm()

    if request.method == "POST":

        form = WhatsAppTestForm(request.POST)

        if form.is_valid():

            phone = form.cleaned_data["phone"]

            try:

                MetaWhatsAppService.send_text_message(

                    phone,

                    "✅ FeeFlow is successfully connected to WhatsApp Cloud API.\n\n"
                    "This message was sent from your FeeFlow application.",

                )

                messages.success(

                    request,

                    "Test WhatsApp message sent successfully.",

                )

            except Exception as e:

                messages.error(

                    request,

                    str(e),

                )

    return render(

        request,

        "whatsapp/test_connection.html",

        {

            "form": form,

        },

    )