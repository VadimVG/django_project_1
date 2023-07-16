from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *


auth_menu=[{'title':'Добавить статью', 'url_name': 'add_article'},
           {'title':'Задать вопрос', 'url_name': 'questions'},
           {'title': 'Выйти', 'url_name': 'logout_user'}]

no_auth_menu=[{'title':'Регистрация', 'url_name':'registration'},
           {'title':'Вход', 'url_name':'login_user'}]


#Главная страница
def index(request):
    articles=Articles.objects.all().order_by('-time_create')
    cats=Categories.objects.all()
    context={
        'title':'Главная страница',
        'auth_menu': auth_menu,
        'no_auth_menu': no_auth_menu,
        'articles': articles,
        'cats': cats,
        'c_selected':0
             }
    return render(request, 'tech_blog/index.html', context=context)


#Показать статьи по категориям
def show_category(request, c_id):
    c_name=Categories.objects.filter(id=c_id)
    articles = Articles.objects.filter(category=c_name[0].name).order_by('-time_create')
    cats = Categories.objects.all()

    if len(articles)==0:
        messages.error(request, 'Статей с такой категорие еще нет')
        return redirect('/')
    else:
        context = {
            'title': 'По категориям',
            'auth_menu': auth_menu,
            'articles': articles,
            'cats': cats,
            'c_selected': c_id
        }
        return render(request, 'tech_blog/index.html', context=context)


#Показать статью полностью
def show_article(request, art_id):
    article=get_object_or_404(Articles, pk=art_id)
    context = {
        'auth_menu': auth_menu,
        'title': article.name,
        'article': article,
        'c_selected': article.category
    }
    return render(request, 'tech_blog/show_article.html', context=context)


#Регистрация
def registration(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth.login(request, user)
            return redirect('home')
    else:
        form=RegistrationForm()
    return render(request, 'tech_blog/registration.html', {'form':form, 'title':'Регистрация'})


#Аутентификация
def login_user(request):
    form = AuthenticationForm()
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Неверный логин и пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'tech_blog/login_user.html', {'form': form, 'title':'Вход'})


#Выход из аккаунта
def logout_user(request):
    auth.logout(request)
    return redirect('login_user')


#Задать вопрос
def questions(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=AddQuestionsForm(request.POST)
            if form.is_valid():
                # print(form.cleaned_data, request.user.id)
                try:
                    user=User.objects.values('id').get(id=request.user.id)
                    theme=form.cleaned_data['theme']
                    text=form.cleaned_data['text']
                    qst=Questions(user_id=user['id'], theme=theme, text=text)
                    qst.save()
                    messages.success(request, 'Вашe сообщение успешно отправлено')
                    return redirect('home')
                except:
                    form.add_error(None, 'Ошибка отправки')
        else:
            form=AddQuestionsForm()

        context={'title':'Задать вопрос',
                  'form':form
                 }
        return render(request, 'tech_blog/questions.html', context=context)
    else:
        messages.error(request, 'Необходимо войти или зарегистрироваться')
        return redirect('/')


#Добавить статью
def add_article(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=AddArticlesForm(request.POST)
            if form.is_valid():
                try:
                    user=User.objects.values('id').get(id=request.user.id)
                    name = form.cleaned_data['name']
                    category=form.cleaned_data['category']
                    text=form.cleaned_data['text']
                    art=Articles(user_id=user['id'], name=name, category=category, text=text)
                    art.save()
                    print(name, category, text, request.user.id)
                    messages.success(request, 'Статья добавлена успешно')
                    return redirect('home')
                except Exception as e:
                    form.add_error(None, 'Ошибка добавления')
                    print(e)
        else:
            form=AddArticlesForm()

        context = {
            'auth_menu': auth_menu,
            'title': 'Добавить статью',
            'form': form
        }
        return render(request, 'tech_blog/add_article.html', context=context)
    else:
        messages.error(request, 'Необходимо войти или зарегистрироваться')
        return redirect('/')