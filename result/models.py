from django.core.validators import MinValueValidator
from django.db import models



# Create your models here.

class DataModel(models.Model):
    user_name = models.CharField(max_length=16,unique='True',verbose_name='유저 이름')
    user_area = models.CharField(max_length=126,verbose_name='지역')
    user_age = models.IntegerField(default=True)
    result_data = models.IntegerField(default=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table='result'
        verbose_name ='탐지데이터'
        verbose_name_plural ='탐지데이터'
