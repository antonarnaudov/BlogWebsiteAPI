from rest_framework import serializers

from blog.models import Like
from blog.serializers.blog_serializers import ShowBlogSerializer
from blog.serializers.user_serializers import UserSimpleSerializer


class ShowLikeSerializer(serializers.ModelSerializer):
    """
    Shows all fields for every Wish.
    Uses UserSimpleSerializer to take only the user id and username.
    Uses ShowPhotosForWishesSerializer to get Photo public fields necessary for the Wishes.
    depth = 1 shows all the data 1 relation deeper
    Suitable for getting all data for the Wishes.
    """
    user = UserSimpleSerializer(help_text='user serializer')
    blog = ShowBlogSerializer(help_text='blog serializer')

    class Meta:
        model = Like
        fields = '__all__'
        depth = 1


class CreateLikeSerializer(serializers.ModelSerializer):
    """
    Shows all fields for every Wish without depth.
    To create or edit requires only User & Photo Id.
    Suitable for creating and editing Wishes.
    """
    class Meta:
        model = Like
        fields = '__all__'
