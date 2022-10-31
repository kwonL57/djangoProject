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
  now = datetime.datetime.now()

  return render(request, 'main.html', {"total":total,"count":count,"lists":lists,"result_count":result_count,"file_list":file_list,"now":now})

def login(request):
  return render(request, 'login.html')

def charts(request):
  return render(request, 'charts.html')

