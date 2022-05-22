from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'login'),
    path('logs/<str:username>', views.LogsView.as_view(), name = 'logs'),


]
