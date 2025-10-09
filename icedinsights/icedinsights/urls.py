# icedinsights/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),                 # Admin panel
    path("accounts/", include("allauth.urls")),      # Auth (login, signup, logout)
    path("", include("dashboard.urls")),             # Custom app (homepage, checkout, etc.)
]
