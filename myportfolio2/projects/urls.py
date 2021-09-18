from django.contrib import admin
from django.urls import include , path
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('',views.projectIndex, name='projectIndex'),
    # path('<slug:slug>/', views.projectDetail,name='project detail')
    # path('Auris/', views.Auris,name='Auris info' ),
    # path('Moddy/', views.Moddy, name='Moddy info'),
    ]