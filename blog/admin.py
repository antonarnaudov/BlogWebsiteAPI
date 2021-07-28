from django.contrib import admin

from blog.models import BlogPost, Like

admin.site.register(BlogPost)
admin.site.register(Like)
