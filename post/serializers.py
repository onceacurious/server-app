from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField
from .models import *


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostSerializer(ModelSerializer):
    tag = PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'tag']

    def create(self, validated_data):
        tags = validated_data.pop('tag')
        post = Post.objects.create(**validated_data)
        for tag in tags:
            tag = Tag.objects.get(pk=tag.id)
            post.tag.add(tag)
        return post
