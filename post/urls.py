from rest_framework.routers import DefaultRouter

from .views import *

app_name = "post"

router = DefaultRouter()

router.register(r'post', PostViewSet, basename='post')
router.register(r'tag', TagViewSet, basename='tag')


urlpatterns = router.urls
