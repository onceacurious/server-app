from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from data.models import *
from .serializers import *

import csv


class UserGroupViewSet(viewsets.ModelViewSet):
    serializer_class = UserGroupSerializer
    queryset = UserGroup.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PositionGroupViewSet(viewsets.ModelViewSet):
    serializer_class = PositionGroupSerializer
    queryset = PositionGroup.objects.all().order_by("title")


class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all().order_by("group", "display_name")


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("name")

    action_map = {
        'upload': 'upload'
    }

    @action(detail=False, methods=['post', 'put'], url_path='upload')
    def upload(self, request, *args, **kwargs):
        csv_file = request.FILES['file']
        reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
        for row in reader:
            _, created = Product.objects.get_or_create(
                name=row['name'], pos_group=row['pos_group'], prod_group=row['prod_group'])

        return Response(status=status.HTTP_201_CREATED)


class UserLevelViewSet(viewsets.ModelViewSet):
    serializer_class = UserLevelSerializer
    queryset = UserLevel.objects.all()

    @action(detail=False, methods=['POST'], url_path='upload')
    def upload(self, request, *args, **kwargs):
        csv_file = request.data
        list = csv_file['file']
        for x in list:
            title = x[0].strip()
            level = x[1].strip()
            disc = x[2].strip()
            if title == '' or level == '' or disc == '':
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                _, created = UserLevel.objects.get_or_create(
                    title=title, level=level, description=disc)
        return Response(status=status.HTTP_201_CREATED)
