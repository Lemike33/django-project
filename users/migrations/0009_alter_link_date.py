# Generated by Django 4.0 on 2021-12-27 19:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_link_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
