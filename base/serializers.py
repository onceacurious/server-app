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
        fields = '__all__'

class UserLevelSerializer(ModelSerializer):
    class Meta:
        model = UserLevel
        fields = '__all__'


class UserUpdateDateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'firs_name', 'last_name', 'email']

class QueSerializer(ModelSerializer):
    class Meta:
        model = Que
        fields = '__all__'