from django.contrib import admin
from django.urls import include , path
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('',views.proectIndex, name='blog index'),
    path('Auris/', views.Auris,name='Auris info' ),
    path('Moddy/' views.Moddy, name='Moddy info'),
    ]