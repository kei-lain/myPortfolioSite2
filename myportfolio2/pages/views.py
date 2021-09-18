from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
	template = 'index.html'
	return render(request, template)

def about_view(request):
	return render(request, 'about/about_index.html')

def contact_view(request):
	name = "Lainey 'Lain' Tubbs"
	emailAddress = "laineytubbs@protonmail.com"
	githubLink = "https://wwww.github.com/kei-lain"

	context = {
		"name" : name,
		"email" : emailAddress,
		"github" : githubLink,

	}
	return render(request, 'contact/contact_index.html', context )
