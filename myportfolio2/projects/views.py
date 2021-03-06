from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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

class projectDetail(DetailView):
	model = Project
	context_object_name = 'project'
	template_name = 'projects/project_detail.html'
# def projectDetail(request):
# 	projects = Project.objects()
# 	context = {
# 		"projects": projects,
# 	}
# 	return(render(request,'	'))
