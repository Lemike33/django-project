# Generated by Django 4.0 on 2022-02-07 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_job_site'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Работа', 'verbose_name_plural': 'Мои работы'},
        ),
    ]