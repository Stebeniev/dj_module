from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mysite.forms import UserRegisterForm, PurchaseCreateForm, ReturnCreateForm
from mysite.models import Product, Purchase, MyUser, Return


class ProductView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = "products"
    paginate_by = 4  ### добавить пагинацию на главную страницу###


class Register(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration_form/signup.html'
    success_url = reverse_lazy('home')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration_form/login.html'

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
    extra_context = {'form': ReturnCreateForm}

    def get_queryset(self):
        if not self.request.user.is_superuser:
            queryset = Purchase.objects.filter(user=self.request.user)
            return queryset
        queryset = Purchase.objects.all()
        return queryset


class PurchaseCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    template_name = 'home.html'
    form_class = PurchaseCreateForm
    success_url = reverse_lazy('purchase')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        product_id = self.kwargs.get('pk')
        product = Product.objects.get(id=product_id)
        object.product = product
        purchase_total = object.quantity * product.price
        if object.quantity > product.quantity:
            messages.error(self.request, "Insufficient quantity of goods in stock")
            return redirect('/')
        elif self.request.user.wallet < purchase_total:
            messages.error(self.request, "You don't have enough money to complete the purchase")
            return redirect('/')
        else:
            product.quantity = product.quantity - object.quantity
            product.save()
            user = MyUser.objects.get(username=self.request.user)
            user.wallet -= purchase_total
            user.save()
        return super().form_valid(form=form)

    # def form_valid(self, form):
        # user = self.request.user
        # product_id = self.kwargs.get('pk')
        # product = Product.objects.get(id=product_id)
        # quantity = int(self.request.POST['quantity'])
        # price = product.price
        # purchase = product.quantity
        # wallet = user.wallet
        # purchase_total = quantity * price
        #
        # if wallet < purchase_total:
        #     messages.error(self.request, "You don't have enough money to complete the purchase")
        #     return redirect('/')
        # if purchase < quantity:
        #     messages.error(self.request, "Insufficient quantity of goods in stock")
        #     return redirect('/')
        #
        # user.wallet -= purchase_total
        # product.quantity -= quantity
        # product = Product.objects.get(id=product_id)
        #
        # with transaction.atomic():
        #     user.save()
        #     product.save()
        #     purchase.save()
        # return super().form_valid(form)
        #
        # object = form.save(commit=False)
        # user = self.request.user
        # product_id = self.kwargs.get('pk')
        # product = Product.objects.get(id=product_id)
        # object.product = product
        # purchase_total = object.quantity * product.price
        # if object.quantity > product.quantity:
        #     messages.error(self.request, "Insufficient quantity of goods in stock")
        #     return redirect('/')
        # elif user.wallet < purchase_total:
        #     messages.error(self.request, "You don't have enough money to complete the purchase")
        #     return redirect('/')
        # else:
        #     product.quantity = product.quantity - object.quantity
        #     product.save()
        #     user = MyUser.objects.get(username=self.request.user)
        #     user.wallet -= purchase_total
        #     user.save()
        #     return super().form_valid(form=form)


class ReturnCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    form_class = ReturnCreateForm
    template_name = 'purchase.html'
    success_url = reverse_lazy('return')

    # def form_valid(self, form):
    #     object = form.save(commit=False)
    #     purchase_id = self.kwargs.get('pk')
    #     purchase = Purchase.objects.get(id=purchase_id)    ###доделать тайминг возврата- вывод сообщения###


class ReturnListView(LoginRequiredMixin, ListView):
    login_url = 'login/'
    model = Return
    template_name = 'return_product.html'
    extra_context = {'form': ReturnCreateForm}
    paginate_by = 4

    def get_queryset(self):
        if not self.request.user.is_superuser:
            queryset = Return.objects.filter(purchase__user=self.request.user)
            return queryset
        queryset = Return.objects.all()
        return queryset


class DeletePurchaseView(LoginRequiredMixin, DeleteView):
    model = Purchase
    success_url = reverse_lazy('return')

    def form_valid(self, form):
        purchase = self.get_object()
        user = purchase.user
        product = purchase.product
        user.wallet += purchase.purchase_total
        product.quantity += purchase.quantity
        return HttpResponseRedirect(self.success_url)


class DeleteReturnView(LoginRequiredMixin, DeleteView):
    model = Return
    success_url = reverse_lazy('return')
