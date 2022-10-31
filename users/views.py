from django.shortcuts import render
from users.models import UsersModel


# Create your views here.
def userslist(request):
    lists = UsersModel.objects.all()
    return render(request, 'userslist.html', {"lists": lists})


