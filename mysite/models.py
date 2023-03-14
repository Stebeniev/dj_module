from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class MyUser(AbstractUser):
    wallet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'
        ordering = ('username', )


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    quantity = models.PositiveIntegerField()

    class Meta:

        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']


    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(MyUser, related_name='purchases', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
        ordering = ['-created']

    def __str__(self):
        return f"{self.product}"

    def purchase_total(self):
        return self.product.price * self.quantity


class Return(models.Model):
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.purchase}'
