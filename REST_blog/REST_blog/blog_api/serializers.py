from rest_framework import serializers

from REST_blog.blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'category', 'title', 'author', 'excerpt', 'content', 'status')
