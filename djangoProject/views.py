# views.py
import os, datetime
from django.shortcuts import render
from users.models import UsersModel
from result.models import DataModel
def main(request):
  total = UsersModel.objects.all()
  count = len(total)
  lists = DataModel.objects.all()
  result_count = len(lists)
  path_dir = '//DESKTOP-GRJCOU7/koren/web'
  file_list = os.listdir(path_dir)
  now_time = datetime.datetime.now()
  result_print = "보이스피싱이 탐지되었습니다."

  return render(request, 'main.html', {"total":total,"count":count,"lists":lists,"result_count":result_count,"file_list":file_list,"now_time":now_time,"result_print":result_print})

def login(request):
  return render(request, 'login.html')

def charts(request):
  return render(request, 'charts.html')

