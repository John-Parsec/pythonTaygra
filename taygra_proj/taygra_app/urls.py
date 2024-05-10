from django.urls import path
from taygra_app import views

urlpatterns = [
    path('', views.home, name='home'),
]