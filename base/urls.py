from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'base'

router = DefaultRouter()
router.register(r'user-group', UserGroupViewSet, basename='user-group'),
router.register(r'user', UserViewSet, basename='user'),
router.register(r'position-group', PositionGroupViewSet, basename='position-group'),
router.register(r'position', PositionViewSet, basename='position'),
router.register(r'product-group', ProductGroupViewSet, basename='product-group'),
router.register(r'product', ProductViewSet, basename='product'),
router.register(r'user-level', UserLevelViewSet, basename='user-level')

urlpatterns = router.urls

