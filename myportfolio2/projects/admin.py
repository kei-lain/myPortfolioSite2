from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'status',)
	list_filter  =  ("status",)
	search_fields = ['title' , 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)

# Register your models here.
