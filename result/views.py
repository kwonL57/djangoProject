from django.shortcuts import render
from result.models import DataModel


# Create your views here.
def resultlist(request):
    lists = DataModel.objects.all()
    # item = {'user_email':list.user_name,
    #         'user_name':list.user_name,
    #         'user_area':list.user_area,
    #         'user_age':list.user_age,
    #         'create_time':list.create_time
    #         }
    result_count = len(lists)

    return render(request, 'main.html', {"lists": lists,"result_count":result_count})

