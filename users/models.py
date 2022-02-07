from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Link(models.Model):
    """ Класс - список всех сокращенных ссылок, по каждому пользователю"""
    user = models.ForeignKey(User, verbose_name='Пользователь', help_text='Укажите пользователя', on_delete=models.CASCADE)
    longLink = models.CharField('Полная ссылка', max_length=160)
    shortLink = models.SlugField('Сокращенная ссылка', max_length=10, unique=True)

    class Meta:
        verbose_name = "Моя ссылка"
        verbose_name_plural = "Мои ссылки"

    def get_absolute_url(self):
        return reverse('links')

    def __str__(self):
        return self.shortLink
