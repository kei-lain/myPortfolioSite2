from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def projectIndex(request):
	return HttpResponse("Index for the project pages")
def Moddy(request):
	return HttpResponse("This will be the page about Moddy")
def Auris(request):
	return HttpResponse("This will be the page for Auris")
