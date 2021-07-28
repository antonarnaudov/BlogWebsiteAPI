from django.contrib.auth.models import User
from django.db import models


class BlogPost(models.Model):
    topic = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)

    image = models.ImageField(upload_to='blog-photos', blank=True)
    content = models.TextField(max_length=3000, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.topic} Blog | {self.title}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like: {self.user.username} | {self.blog.title}'
