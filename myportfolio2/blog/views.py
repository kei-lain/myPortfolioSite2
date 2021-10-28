from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
# def indexer(request):
# 	return HttpResponse("Index for Le Bloguette")
# class postList(generic.ListView):
# 	posts = Post.objects.all()
# 	queryset = posts.order_by('-created_on')
# 	template_name = 'base_index.html'
class postView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'base_index.html'
	# def get_context_data(self, **kwargs):
	#     context = super().get_context_data(**kwargs)
	#     context['posts'] = context['posts'].filter('-created_on')
	#     return context
class postDetail(DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'post_detail.html'




