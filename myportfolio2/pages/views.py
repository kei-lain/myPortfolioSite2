from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("This is the index for my portfolio site!")

def about_view(request):
	return HttpResponse("This is the about me page.")

def contact_view(request):
	return HttpResponse("This is the contact info page.")

def project_view(request):
	return HttpResponse("This is the projects home page")

def blog_view(request):
	return HttpResponse("This is the blog page")