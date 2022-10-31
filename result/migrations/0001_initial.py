# Generated by Django 4.1.2 on 2022-10-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')),
                ('user_pw', models.CharField(max_length=128, verbose_name='유저 비밀번호')),
                ('user_name', models.CharField(max_length=16, unique='True', verbose_name='유저 이름')),
                ('user_area', models.CharField(max_length=126, verbose_name='지역')),
                ('user_age', models.IntegerField(default=True)),
                ('result_data', models.IntegerField(default=True)),
            ],
            options={
                'verbose_name': '탐지데이터',
                'verbose_name_plural': '탐지데이터',
                'db_table': 'result',
            },
        ),
    ]
