from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.invoice_list,
        name="invoice_list"
        ),
    path(
        "receive/<uuid:invoice_id>/",
        views.receive_payment, 
        name="receive_payment"
        ),
    
    path(
    "pending/",
    views.pending_payments,
    name="pending_payments",
    ),

path(
    "verify/<int:payment_id>/",
    views.verify_payment,
    name="verify_payment",
),
]


