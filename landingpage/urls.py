from django.urls import path

from . import views

urlpatterns = [
    path('landingpage-devlopment', views.landingpage, name='landingpage'),
]