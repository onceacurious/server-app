from rest_framework.serializers import ModelSerializer
from data.models import *

class UserGroupSerializer(ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['password']

class PositionGroupSerializer(ModelSerializer):
    class Meta:
        model = PositionGroup
        fields = '__all__'

class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class ProductGroupSerializer(ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product