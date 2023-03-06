from rest_framework import routers

from mysite.api.resources import ProductViewSet, UserViewSet

router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
router.register(r'customer', UserViewSet)


urlpatterns = router.urls