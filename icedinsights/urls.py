from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coffee.urls')),  # ✅ route homepage to dashboard
    path('accounts/', include('allauth.urls')),  # ✅ Allauth login/signup
]
