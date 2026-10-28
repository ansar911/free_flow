from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.billing_dashboard,
        name="billing_dashboard",
    ),

    path(
        "generate/",
        views.generate_billing,
        name="generate_billing",
    ),

    path(
        "pay/<uuid:token>/",
        views.parent_payment,
        name="parent_payment",
    ),

    path(
        "pay/<uuid:token>/submit/",
        views.submit_payment,
        name="submit_payment",
    ),

]