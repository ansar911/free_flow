from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


@login_required
def billing_dashboard(request):
    return HttpResponse("Billing Dashboard - Coming Soon")


@login_required
def generate_billing(request):
    return HttpResponse("Generate Billing - Coming Soon")