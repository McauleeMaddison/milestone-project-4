from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def health(request):
    return HttpResponse("OK")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.dashboard.urls")),
    path("products/", include("apps.products.urls")),
    path("payments/", include("apps.payments.urls")),
    path("health/", health),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)