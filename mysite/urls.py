from django.urls import path
from .views import ProductView, Register, Login, Logout

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('signup/', Register.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout')
]
