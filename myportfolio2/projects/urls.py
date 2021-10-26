from django.contrib import admin
from django.urls import include , path
from .views import projectIndex , projectDetail 
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('',projectIndex.as_view(), name='projectIndex'),
    path('<slug:slug>', projectDetail.as_view(), name = 'project-detail')
    # path('<slug:slug>/', views.projectDetail,name='project detail')
    # path('Auris/', views.Auris,name='Auris info' ),
    # path('Moddy/', views.Moddy, name='Moddy info'),
    ]