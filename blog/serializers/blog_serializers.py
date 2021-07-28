from rest_framework import serializers

from blog.models import BlogPost
from blog.serializers.user_serializers import UserSimpleSerializer


class ShowBlogSerializer(serializers.ModelSerializer):
    """
    Shows Public Blog data required for Likes page.
    """
    author = UserSimpleSerializer(help_text='user serializer')

    class Meta:
        model = BlogPost
        exclude = ('content',)
        depth = 1


class CreateBlogSerializer(serializers.ModelSerializer):
    """
    Shows all fields necessary for Blog Update.
    Makes image field Not required.
    Suitable for editing and updating Blog.
    """

    class Meta:
        model = BlogPost
        fields = '__all__'
        extra_kwargs = {'image': {'required': False, 'allow_null': True}}


class DetailedBlogSerializer(serializers.ModelSerializer):
    """
    Shows all Public fields for every Blog.
    """
    author = UserSimpleSerializer(help_text='user serializer')

    class Meta:
        model = BlogPost
        fields = '__all__'
        depth = 1
