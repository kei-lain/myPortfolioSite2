from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.urls import reverse


# Create your views here.

def projectIndex(request):
	projects = Project.objects.all()
	context = {
		"projects" : projects,
			}
	return render(request, 'projects/project_index.html',context)
# def projectDetail(request):
# 	projects = Project.objects()
# 	context = {
# 		"projects": projects,
# 	}
# 	return(render(request,'	'))
