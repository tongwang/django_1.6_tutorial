from django.contrib import admin

# Register your models here.
from dj_tutorial.apps.blogs.models import Blog, Author, Entry
    
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)