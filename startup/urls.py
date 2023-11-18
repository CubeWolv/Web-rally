from django.urls import path

from . import views

urlpatterns = [
    path('startup-devlopment', views.startup, name='startup'),
]