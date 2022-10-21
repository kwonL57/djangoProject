from django.shortcuts import render
from users.models import UsersModel


# Create your views here.
def userslist(request):
    lists = UsersModel.objects.all()
    # item = {'user_email':list.user_name,
    #         'user_name':list.user_name,
    #         'user_area':list.user_area,
    #         'user_age':list.user_age,
    #         'create_time':list.create_time
    #         }

    return render(request, 'userslist.html',{"lists":lists})

