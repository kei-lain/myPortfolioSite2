from django.contrib import admin
from django.urls import include , path
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('',views.postList, name='blog index'),
    path('<slug:slug>/', views.postDetail,name='post detail' ),