# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.trends, name='home'),
    path('checkout/', views.create_checkout_session, name='checkout'),
    path('webhook/', views.stripe_webhook, name='stripe-webhook'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]