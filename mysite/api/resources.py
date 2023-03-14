from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.viewsets import ModelViewSet

from rest_framework import permissions
from rest_framework.authtoken.models import Token

from mysite.api.permissions import IsAdminOrReadOnly
from mysite.models import Product, Purchase, MyUser, Return
from mysite.api.serializers import ProductSerializer, PurchaseSerializer, MyUserSerializer, ReturnSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    ordering_fields = ['name', 'quantity', 'price']
    permission_classes = (IsAdminOrReadOnly, )
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)



class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class UserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class ReturnViewSet(ModelViewSet):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer


