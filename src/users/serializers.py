from rest_framework import serializers
from .models import Profile
from posts.models import Post
from django.contrib.auth.models import User
from posts.serializers import PostSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # profile = serializers.HyperlinkedRelatedField(  # new
    #     many=False, view_name='profile-detail', read_only=True)
    bio = serializers.ReadOnlyField(source='profile.bio')
    date_joined = serializers.ReadOnlyField(source='profile.date_joined')
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'username', 'bio', 'date_joined', 'posts']




class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ['id', 'url', 'user', 'username', 'email', 'bio', 'date_joined']
