from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser, FileUploadParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from blog.mixins import SerializerRequestSwitchMixin
from blog.models import BlogPost
from blog.serializers.blog_serializers import CreateBlogSerializer, DetailedBlogSerializer, ShowBlogSerializer


class BlogViewSet(SerializerRequestSwitchMixin, ModelViewSet):
    """
    ViewSet supporting all operations for Wishes.
    """
    queryset = BlogPost.objects.all()
    serializers = {
        'show': ShowBlogSerializer,
        'create': CreateBlogSerializer,
        'update': CreateBlogSerializer,
        'detailed': DetailedBlogSerializer,
    }

    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('topic', 'title')
    filterset_fields = ['author__username', ]
    ordering_fields = ''
    ordering = '-id'

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data['author'] = user.pk
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = request.user
        request.data['author'] = user.pk
        return super().update(request, *args, **kwargs)
    