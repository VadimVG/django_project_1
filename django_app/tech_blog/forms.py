from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddQuestionsForm(forms.Form):
    theme=forms.ModelChoiceField(queryset=ThemesQuestions.objects.all(), label='Тема')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст')


class AddArticlesForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категория')
    name=forms.CharField(max_length=250, label='Название статьи')
    text=forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}),label='Содержимое статьи')


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')



