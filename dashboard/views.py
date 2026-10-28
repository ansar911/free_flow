from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .services.dashboard_info import DashboardService


@login_required
def dashboard(request):

    context = DashboardService.get_dashboard()

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )