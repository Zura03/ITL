from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('createbook/', views.createbook, name='createbook'),
    path('index', views.indexprod, name='add'),
    path('createprod/', views.createprod, name='createprod'),
    path('addprod/', views.addprod, name='addprod'),
    path('addhuman/', views.addhuman, name='addhuman'),
    path('createhuman/', views.createhuman, name='createhuman'),
    path('update/', views.update, name='update'),
]