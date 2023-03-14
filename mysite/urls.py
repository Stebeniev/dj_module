from django.urls import path, include

from mysite.views import ProductView, Register, Login, Logout, ProductCreateView, ProductUpdateView,   \
    PurchaseCreateView, PurchaseListView, ReturnListView, ReturnCreateView, PurchaseDeleteView, ReturnDeleteView



urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('signup/', Register.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('new/product', ProductCreateView.as_view(), name='new_product'),
    path('update/product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('purchase/create/<int:pk>', PurchaseCreateView.as_view(), name='purchase_create'),
    path('purchase/', PurchaseListView.as_view(), name='purchase'),
    path('return/', ReturnListView.as_view(), name='return'),
    path('return/product/<int:pk>', ReturnCreateView.as_view(), name='return_product'),
    path('return/delete/<int:pk>/', PurchaseDeleteView.as_view(), name='delete_return'),
    path('delete/<int:pk>/', ReturnDeleteView.as_view(), name='delete'),

    # path('api/', include('mysite.api.urls'))
]
