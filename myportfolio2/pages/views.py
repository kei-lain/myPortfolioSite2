from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
	template = 'index.html'
	return render(request, template)

def about_view(request):
	return HttpResponse("This is the about me page.")

def contact_view(request):
	return HttpResponse("This is the contact info page.")

def project_view(request):
	return HttpResponse("This is the projects home page")

def blog_view(request):
	return HttpResponse("This is the blog page")