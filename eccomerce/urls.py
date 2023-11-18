from django.urls import path

from . import views

urlpatterns = [
    path('eccomerce-devlopment', views.eccomerce, name='eccomerce'),
]