from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from blog.models import BlogPost, Like
from blog.tests.factory import BlogFactory, LikeFactory


class BlogTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test')
        self.blog = BlogFactory.create(author=self.user)
        self.blog.save()

    def test_has_model(self):
        """
        Has Blog
        """
        blog = BlogPost()
        self.assertIsInstance(blog, BlogPost)

    def test_can_create(self):
        """
        Can save blogs properly
        """
        self.assertIsInstance(self.blog, BlogPost)
        self.assertEqual(self.blog.topic, BlogFactory.topic)
        self.assertEqual(self.blog.title, BlogFactory.title)
        self.assertEqual(self.blog.content, BlogFactory.content)
        self.assertEqual(self.blog.author, self.user)


class LikeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test')
        self.user2 = User.objects.create_user('test2')
        self.blog = BlogFactory.create(author=self.user)
        self.like = LikeFactory.create(blog=self.blog, user=self.user2)
        self.like.save()

    def test_has_model(self):
        """
        Has Like
        """
        like = Like()
        self.assertIsInstance(like, Like)

    def test_can_create(self):
        """
        Can save likes properly
        """
        self.assertIsInstance(self.like, Like)
        self.assertNotEqual(self.like, self.like.blog.author)
        self.assertEqual(self.like.blog, self.blog)
        self.assertEqual(self.like.user, self.user2)
        self.assertEqual(self.blog.author, self.user)
