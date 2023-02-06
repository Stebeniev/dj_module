from django.contrib import admin
from mysite.models import MyUser, Product, Purchase, Return
from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser, UserAdmin)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Return)


