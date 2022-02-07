from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Link


class UserRegisterForm(UserCreationForm):
    """ стандартная форма заполнения регистрации исключая подтверждение пароля"""
    email = forms.EmailField(label='Введите Email', required=True,
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Введите ваш Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        exclude = ['password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    """ Класс для обновления полей email, username таблицы user"""
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput()
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class LinkForm(forms.ModelForm):
    """ Веб-ресурс для, для добавления сокращаемых ссылок на сайт"""
    class Meta:
        model = Link
        # все поля из таблицы Link
        fields = ['user', 'longLink', 'shortLink']

        # поле user отображать не будем
        widgets = {'user': forms.HiddenInput()}

