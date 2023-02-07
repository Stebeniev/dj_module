from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from mysite.forms import UserRegisterForm
from mysite.models import Product


class ProductView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = "products"


class Register(CreateView):
    form_class = UserRegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class Logout(LogoutView):
    pass
