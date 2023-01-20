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

    class Meta:
        model = User
        fields = ["username", "first_name",
                  "last_name", "company", "display_name", "position", "level"]
        read_only_fields = ["password", "display_name"]

    def create(self, validated_data):
        user_group = validated_data.pop("company")
        company = UserGroup.objects.get(pk=user_group.id)
        user = User.objects.create(company=company, **validated_data)
        return user

    def get_display_name(self, obj):
        return obj.company.display_name


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
