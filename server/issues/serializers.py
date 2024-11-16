from rest_framework import serializers
from .models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source="author.id", read_only=True)

    class Meta:
        model = Post
        fields = ('author',
                  'title',
                  'content',
                  'views',)

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id",
                  "author",
                  "title",
                  "content",
                  'views',)


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id",
                  "author",
                  "title",
                  "content",
                  'views',)
