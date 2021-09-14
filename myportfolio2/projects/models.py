from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse,NoReverseMatch  
# Create your models here.

STATUS = (
	(0, "Working!"),
	(1, "Finished")
	)


class Project(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	projectlink = models.URLField(max_length=200)
	language = models.TextField(max_length=40)
	updated_on = models.DateTimeField(auto_now=True)
	about = models.TextField()
	status = models.IntegerField(choices=STATUS, default=0)

	# def get_absolute_url(self):
 #    	return reverse('postDetail', kwargs={'slug': self.slug}) 
    # slug = models.SlugField(max_length=200)
    
    # projectlink = models.URLField(**kwargs)
    # language = models.TextField()
    # about = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    # language = models.TextField()