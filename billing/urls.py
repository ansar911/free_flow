from django.urls import path
from . import views

urlpatterns = [
    path("", views.billing_dashboard, name="billing_dashboard"),
    path("generate/", views.generate_billing, name="generate_billing"),
]