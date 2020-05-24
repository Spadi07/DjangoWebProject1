"""
Definition of forms.
"""

#3 работа
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

#5работа
from django.db import models
from .models import Comment

#6работа 
from .models import Post, Order

#Форма заказа
from django.utils import timezone





class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':"Комментарий"}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description','content','image',)
        labels = {'title':"Заголовок", 'description': "Краткое описание", 'content': "Полное содержание", 'image': "Изображение"}


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {'first_name','last_name','phone','address','buying_type','comments', 'size'}
        labels = {'first_name': "Имя",'last_name': 'Фамилия',
                  'phone': 'Контактный телефон','address': 'Адрес доставки',
                  'buying_type': 'Способ доставки',
                  'comments': 'Комментарии к заказу', 'size': 'Размер обуви'}
