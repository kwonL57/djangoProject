# Generated by Django 4.1.2 on 2022-11-03 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_usersmodel_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='create_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='생성 시간'),
        ),
    ]
