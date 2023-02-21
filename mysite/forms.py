from django import forms
from django.core.exceptions import ValidationError
from mysite.models import MyUser
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username:', widget=forms.TextInput)
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm the password:', widget=forms.PasswordInput)
    wallet = forms.DecimalField(initial=10000, widget=forms.HiddenInput)

    class Meta:
        model = MyUser
        fields = '__all__'

    def clean(self):
        username = self.cleaned_data.get('username')
        if MyUser.objects.filter(username=username).exists():
            raise ValidationError('User with this name is already registered')



