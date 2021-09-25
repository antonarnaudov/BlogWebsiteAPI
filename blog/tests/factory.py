from django.contrib.auth.models import User
from factory import SubFactory
from factory.django import DjangoModelFactory

from blog.models import BlogPost, Like


class BlogFactory(DjangoModelFactory):
    class Meta:
        model = BlogPost

    topic = 'Test topic'
    title = 'Test title'
    content = 'Test content for the blog test.'


class LikeFactory(DjangoModelFactory):
    class Meta:
        model = Like
