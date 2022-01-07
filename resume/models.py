from django.db import models
from PIL import Image
from django.urls import reverse
from django.utils import timezone


class Job(models.Model):
    slug = models.SlugField(unique=True)  # url адресс перехода на детальную страницу работы
    title = models.CharField(max_length=140)
    description = models.TextField()
    img = models.ImageField(default='default.png', upload_to='work_images')
    date_start = models.DateField('Начало работы', default=timezone.now)
    date_end = models.DateField('Окончание работы', default=timezone.now)
    site = models.URLField(max_length=200, default='www')

    def __str__(self):
        return self.title

