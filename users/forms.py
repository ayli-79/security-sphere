from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Обязательное поле.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Обязательное поле.')
    patronymic = forms.CharField(max_length=30, required=True, help_text='Обязательное поле.')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'patronymic', 'password1', 'password2')
