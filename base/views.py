from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status  
from django.shortcuts import get_object_or_404

from data.models import *
from .serializers import *



class UserGroupViewSet(viewsets.ModelViewSet):
    serializer_class = UserGroupSerializer
    queryset = UserGroup.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PositionGroupViewSet(viewsets.ModelViewSet):
    serializer_class = PositionGroupSerializer
    queryset = PositionGroup.objects.all()

class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

class ProductGroupViewSet(viewsets.ModelViewSet):
    serializer_class = ProductGroupSerializer
    queryset = ProductGroup.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
