from rest_framework import routers

from mysite.api.resources import ProductViewSet, UserViewSet, PurchaseViewSet, ReturnViewSet

router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
router.register(r'user', UserViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'return', ReturnViewSet)


urlpatterns = router.urls