from django.urls import path
from App import views

urlpatterns = [
    path('', views.home),
    path('submit', views.submit),
]