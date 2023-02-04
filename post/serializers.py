from rest_framework.serializers import ModelSerializer
from .models import *


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostSerializer(ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "tag"]
