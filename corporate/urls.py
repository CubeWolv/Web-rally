from django.urls import path

from . import views

urlpatterns = [
    path('coporate-devlopment', views.corporate, name='corporate'),
]