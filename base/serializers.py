from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField, StringRelatedField
from data.models import *


class UserGroupSerializer(ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"


class PositionSerializer(ModelSerializer):

    group = PrimaryKeyRelatedField(many=False, queryset= PositionGroup.objects.all())
    group_name = SerializerMethodField()
    class Meta:
        model = Position
        fields = ["id", "display_name", "group", "group_name"]
        ordering_fields = ["display_name"]
        read_only_fields = ["id", "group_name"]

    def create(self, validated_data):
        group = validated_data.pop("group")
        display_name = validated_data.pop("display_name")
        group_name = PositionGroup.objects.get(pk=group.id)
        position = Position.objects.create(group=group_name, display_name= display_name.strip().lower())
        return position

    def get_group_name(self, obj):
        return obj.group.title

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
        fields = ["id","username", "first_name",
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

    def create(self, validated_data):
        title = validated_data.pop("title")
        position_group = PositionGroup.objects.create(title=title.strip().lower(), **validated_data)
        return position_group


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
