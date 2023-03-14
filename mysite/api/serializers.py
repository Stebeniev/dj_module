from rest_framework import serializers
from mysite.models import Product, Purchase, MyUser, Return


class MyUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model: MyUser
        fields = ['id', 'username', 'password1', 'password2', 'wallet']

    def save(self):
        user = MyUser(
            username=self.validated_data['username'],
            wallet=10000
        )
        password = self.validated_data['password'],
        password2 = self.validated_data['password2'],
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must by match'})
        user.set_password(password)
        user.save()
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']


class PurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Purchase
        fields = ['user', 'product', 'quantity']
        read_only_fields = ['user']


class ReturnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Return
        fields = ['id', 'purchase', 'created']





