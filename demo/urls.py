from django.contrib import admin
from django.urls import path
from .views import index, add_visitor


urlpatterns = [
    path('',index, name='index'),
    path('visitor/',add_visitor ,name='add_visitor')
]