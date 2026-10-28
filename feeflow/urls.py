from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),
    path("students/", include("students.urls")),
    path("parents/", include("parents.urls")),
    path("billing/", include("billing.urls")),
    path("payments/", include("payments.urls")),
    path("settings/", include("settings_app.urls")),
    path("reports/", include("reports.urls")),
    path("whatsapp/", include("whatsapp.urls")),
    path("accounts/", include("user_management.urls"),),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
