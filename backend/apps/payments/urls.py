from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.create_payment, name='checkout'),
    path('ipn/', views.ipn_callback, name='ipn_callback'),
    path('success/', views.payment_success, name='payment_success'),
]
