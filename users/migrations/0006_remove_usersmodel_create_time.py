# Generated by Django 4.1.2 on 2022-11-03 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_usersmodel_create_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersmodel',
            name='create_time',
        ),
    ]
