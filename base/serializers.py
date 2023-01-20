from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField, StringRelatedField
from data.models import *


class UserGroupSerializer(ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class UserSerializer(ModelSerializer):
    company = PrimaryKeyRelatedField(
        many=False, queryset=UserGroup.objects.all())
    display_name = SerializerMethodField()

    position = PrimaryKeyRelatedField(
        many=False, queryset=Position.objects.all()
    )
    position_title = SerializerMethodField()

    level = PrimaryKeyRelatedField(
        many=False, queryset=UserLevel.objects.all()
    )

    level_title = SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "first_name",
                  "last_name", "company", "display_name", "position", "position_title", "level", "level_title"]
        read_only_fields = ["password", "display_name",
                            "position_title", "level_title"]

    def create(self, validated_data):
        user_group = validated_data.pop("company")
        company = UserGroup.objects.get(pk=user_group.id)
        position_title = validated_data.pop("position")
        position = Position.objects.get(pk=position_title.id)
        level_title = validated_data.pop("level")
        level = UserLevel.objects.get(pk=level_title.id)
        user = User.objects.create(
            company=company, position=position, level=level, **validated_data)
        return user

    def get_display_name(self, obj):
        return obj.company.display_name

    def get_position_title(self, obj):
        return obj.position.display_name

    def get_level_title(self, obj):
        return obj.level.title


class PositionGroupSerializer(ModelSerializer):
    class Meta:
        model = PositionGroup
        fields = "__all__"


class ProductGroupSerializer(ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UserLevelSerializer(ModelSerializer):
    class Meta:
        model = UserLevel
        fields = "__all__"


class UserUpdateDateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["password", "firs_name", "last_name", "email"]


class QueSerializer(ModelSerializer):
    class Meta:
        model = Que
        fields = "__all__"
