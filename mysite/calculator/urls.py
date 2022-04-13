from django.urls import path
from . import views

urlpatterns = [
    path('calculator/calculate', views.calculate)
]
