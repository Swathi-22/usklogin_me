from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("app/", include("registration.backends.simple.urls")),
        path("", include("web.urls", namespace="web")),
        path("", include("services.urls", namespace="services")),
        path("", include("invoices.urls", namespace="invoices")),
        path("tinymce/", include("tinymce.urls")),
        path("OneSignalSDKWorker.js", TemplateView.as_view(template_name="OneSignalSDKWorker.js", content_type="application/javascript")),
        path("", include("user_sessions.urls", "user_sessions")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
admin.site.site_header = "USKLOGIN Administration"
admin.site.site_title = "USKLOGIN Admin Portal"
admin.site.index_title = "Welcome to USKLOGIN Admin Portal"
