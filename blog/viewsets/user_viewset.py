from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from blog.mixins import SerializerRequestSwitchMixin
from blog.serializers.user_serializers import RegisterSerializer, UserSerializer, UserSimpleSerializer, \
    UpdateUserSerializer


class UserViewSet(SerializerRequestSwitchMixin, ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializers = {
        'show': UserSimpleSerializer,
        'create': RegisterSerializer,
        'update': UpdateUserSerializer,
        'detailed': UserSerializer
    }
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })