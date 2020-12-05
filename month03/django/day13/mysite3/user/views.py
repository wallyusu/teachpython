from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def add_user(request):
    return HttpResponse('添加用户')

def index_view(request):
    return render(request,'index.html')