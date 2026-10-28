from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.whatsapp_dashboard,
        name="whatsapp_dashboard",
    ),

    path(
        "generate/",
        views.generate_queue,
        name="generate_queue",
    ),

    path(
    "test/",
    views.test_connection,
    name="whatsapp_test",
    ),

]