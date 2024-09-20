from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('createpage/', views.create, name='create'),
    path('home/', views.home, name='home'),
    path('home/add/', views.add, name='add'),
]
