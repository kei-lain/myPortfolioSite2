from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic


# Create your views here.
# def indexer(request):
# 	return HttpResponse("Index for Le Bloguette")
# class postList(generic.ListView):
# 	posts = Post.objects.all()
# 	queryset = posts.order_by('-created_on')
# 	template_name = 'base_index.html'
def postList(request):
	posts = Post.objects.all()
	queryset = posts.order_by('-created_on')
	context = {
		"posts" : posts,
		"queryset": queryset, 
	}
	return render(request, 'base_index.html', context)
	
				
		
def postDetail(request):
 	posts = Post.objects()
# class postDetail(generic.ListView):
 	template_name = 'post_detail.html'
 	context = {
 	"model": model,
 	}
 	return(render(request,'post_detail.html',context))




