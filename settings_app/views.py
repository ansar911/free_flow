from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import AcademySettings
from .forms import AcademySettingsForm


@login_required
def settings_view(request):

    settings = AcademySettings.objects.first()

    if settings is None:

        settings = AcademySettings.objects.create()

    if request.method == "POST":

        form = AcademySettingsForm(

            request.POST,

            request.FILES,

            instance=settings,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Settings saved successfully.",

            )

            return redirect("settings")

    else:

        form = AcademySettingsForm(

            instance=settings,

        )

    whatsapp_ready = (

        settings.whatsapp_enabled

        and bool(settings.whatsapp_access_token)

        and bool(settings.whatsapp_phone_number_id)

        and bool(settings.whatsapp_business_account_id)

    )

    return render(

        request,

        "settings/settings.html",

        {

            "form": form,

            "settings": settings,

            "whatsapp_ready": whatsapp_ready,

        },

    )