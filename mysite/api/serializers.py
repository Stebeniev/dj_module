from rest_framework import serializers
from mysite.models import Product, Purchase, MyUser



class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model: MyUser
        fields = ['username']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']


class PurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ['user', 'product', 'quantity']







