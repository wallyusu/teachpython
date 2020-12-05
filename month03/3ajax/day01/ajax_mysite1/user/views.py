import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User
from django.core import serializers


# Create your views here.
def get_users(request):
    users = User.objects.all()
    # 方式一
    # json_str = serializers.serialize('json', users)
    # return HttpResponse(json_str,content_type='application/json')
    # 方式二
    res =[]
    for user in users:
        u_data = {}
        u_data['username'] = user.username
        u_data['age'] = user.age
        res.append(u_data)
    # json_str = json.dumps(res)
    # return HttpResponse(json_str,content_type='application/json')
    return JsonResponse(res,safe=False)

def index_users(request):
    return render(request,'user_index.html')