from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculate),
    path('', views.IndexView.as_view()),
    path('foodtype/', views.foodType)
]
