from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'date_created']

        # read_only = []