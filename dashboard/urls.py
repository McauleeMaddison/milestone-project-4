from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customize/<int:product_id>/', views.customize_product, name='customize_product'),
    path('settings/', views.user_settings, name='user_settings')
]
