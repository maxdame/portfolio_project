from django.urls import path
from customers import views

urlpatterns = [
    path('customers/', views.index),
]
