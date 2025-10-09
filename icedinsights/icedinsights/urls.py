from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),                     # Admin panel
    path("accounts/", include("allauth.urls")),          # Allauth login/register/logout
    path("", include("dashboard.urls")),                 # Dashboard app (homepage + checkout)
]
