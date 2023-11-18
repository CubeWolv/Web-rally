from django.urls import path

from . import views

urlpatterns = [
    path('wordpress-development', views.wordpress, name='wordpress'),
]