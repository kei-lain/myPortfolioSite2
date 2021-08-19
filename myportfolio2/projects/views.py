from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def projectIndex(request):
	return HttpResponse("Index for the project pages")