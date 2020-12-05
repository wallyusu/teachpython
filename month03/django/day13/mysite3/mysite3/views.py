from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index_view(request):
    name = 'tedu'
    return render(request,'base.html',locals())

def news_view(request):
    return render(request,'news.html')

def sports_view(request):
    return render(request,'sports.html')

def military_view(request):
    # return render(request,'military.html')

    # 视图函数中使用url反向解析
    url = reverse('pgn',args=[200])
    print(url)
    return HttpResponse(url)

def pagen_view(request,n):
    return HttpResponse('pagen:%s'% n)

def test_static(request):
    return render(request,'test_static.html')