from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply, name='apply'),
    path('apply/success/', views.apply_success, name='apply_success'),
]
