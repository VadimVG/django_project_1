from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Categories(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    time_create=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('category', kwargs={'c_id':self.pk})


class Articles(models.Model):
    # user= models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    category=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    text=models.TextField(blank=True)
    time_create=models.DateTimeField(auto_now_add=True)


class ThemesQuestions(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    time_create=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('theme', kwargs={'c_id':self.pk})


class Questions(models.Model):
    # user= models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    theme=models.CharField(max_length=250, blank=True)
    text = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

