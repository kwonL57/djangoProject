from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


# Create your models here.

class UsersModel(models.Model):
    user_email = models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')
    user_pw = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=16,unique='True',verbose_name='유저 이름')
    user_area = models.CharField(max_length=126,verbose_name='지역')
    user_age = models.IntegerField(default=True)
    create_time = models.DateTimeField(default=timezone.now,verbose_name='생성 시간')
    user_phone = models.CharField(max_length=16, blank=True, null=True, verbose_name='전화번호')
    def __str__(self):
        return self.user_name

    class Meta:
        db_table='users'
        verbose_name ='유저'
        verbose_name_plural ='유저'
