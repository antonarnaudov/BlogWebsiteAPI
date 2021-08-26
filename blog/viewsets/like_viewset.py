from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from blog.mixins import SerializerRequestSwitchMixin

# NOTE: ordering_fields does NOT support nested fields
from blog.models import Like
from blog.serializers.like_serializers import ShowLikeSerializer, CreateLikeSerializer


class LikeViewSet(SerializerRequestSwitchMixin, ModelViewSet):
    """
    ViewSet supporting all operations for Wishes.
    """
    serializers = {
        'show': ShowLikeSerializer,
        'create': CreateLikeSerializer,
        'update': CreateLikeSerializer,
    }

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('blog__topic', 'blog__title')
    ordering_fields = ''
    filterset_fields = ['blog__id', ]
    ordering = '-blog_id'

    def get_queryset(self):
        """
        Filtering for the current User
        """
        queryset = Like.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        blog = request.data['blog']
        request.data['user'] = request.user.pk
        like = Like.objects.filter(user=request.user, blog=blog)

        if like.exists():
            like.delete()
            return Response('', status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)
