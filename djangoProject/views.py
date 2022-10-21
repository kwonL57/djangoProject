# views.py

from django.shortcuts import render
from users.models import UsersModel

def main(request):
  total = UsersModel.objects.all()
  count = len(total)
  return render(request, 'main.html', {"total":total,"count":count})

def login(requset):
  return render(requset, 'login.html')

def charts(requset):
  return render(requset, 'charts.html')