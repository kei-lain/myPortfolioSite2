from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.urls import reverse
from django.views.generic.list import ListView

# Create your views here.

# def projectIndex(request):
# 	projects = Project.objects.all()
# 	context = {
# 		"projects" : projects,
# 			}
# 	return render(request, 'projects/project_index.html',context)

class projectIndex(ListView):
	model = Project
	context_object_name = 'projects'
	template_name = 'projects/project_index.html'
	
# def projectDetail(request):
# 	projects = Project.objects()
# 	context = {
# 		"projects": projects,
# 	}
# 	return(render(request,'	'))
