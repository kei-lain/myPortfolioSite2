from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic

# Create your views here.
# def indexer(request):
# 	return HttpResponse("Index for Le Bloguette")
def postList(request):
		queryset = Post.objects.filter(status=1).order_by('-created_on')
		template_name = 'blog_index.html'
		return HttpResponse(queryset)

def postDetail(self):
	model= Post
	template_name = 'Post_detail.html'
