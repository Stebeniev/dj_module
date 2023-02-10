from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages

from mysite.forms import UserRegisterForm, PurchaseCreateForm
from mysite.models import Product, Purchase, MyUser


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
    next_page = 'home'


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'new_product.html'
    success_url = reverse_lazy('new_product')


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'update_product.html'
    success_url = reverse_lazy('home')


class PurchaseListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Purchase
    template_name = 'purchase.html'
    # extra_context = {'form': PurchaseCreateForm}
    # extra_context = {'create_form': PurchaseCreateForm()}

    def get_queryset(self):
        if not self.request.user.is_superuser:
            queryset = Purchase.objects.filter(user=self.request.user)
            return queryset
        queryset = Purchase.objects.all()
        return queryset


class PurchasesCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Purchase
    form_class = PurchaseCreateForm
    template_name = 'home.html'
    success_url = reverse_lazy('purchases')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        product = Product.objects.get(id=self.request.POST['product_pk'])
        object.product = product
        object.save()
        return super().form_valid(form=form)






