from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from mysite.models import Product, Purchase, MyUser
from mysite.api.serializers import ProductSerializer, PurchaseSerializer, MyUserSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class UserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


