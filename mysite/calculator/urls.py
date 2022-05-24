from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'login'),
    path('logs/<str:username>', views.LogsView.as_view(), name = 'logs'),
    path('create/<str:username>', views.CreateRate.as_view(), name = 'create'),
    path('create/<str:username>/rate', views.SaveRate.as_view(), name = 'save'),
    path('profile/<str:username>', views.ProfileView.as_view(), name = 'profile'),
    path('profile/<str:username>/edit', views.EditView.as_view(), name = 'edit'),
]
