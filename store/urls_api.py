from rest_framework import routers
from .serializers import BookSerializer
from .views_api import BookViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = router.urls
