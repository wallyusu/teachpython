from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json


def test_xhr(request):
    return render(request, 'test_xhr.html')


def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')


def test_xhr_get_server(request):
    return HttpResponse('this is Ajax Date')


def test_jq_get(request):
    return render(request, 'test_jq_get.html')


def test_jq_get_server(request):
    return HttpResponse('this is Ajax Data,JQ!')


def test_json(request):
    return render(request, 'test_json.html')


def make_json_server(request):
    # 字典
    # map1 = {"name": "tedu", "age": 18}
    # return JsonResponse(map1, safe=True)
    # 列表,元组
    list1 = [
        {'name': "tedu", "age": 18},
        {"name": "tarena", "age": 20}
    ]
    return JsonResponse(list1, safe=False)


# 注册
def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        print(uname)
        print(pwd)
        return HttpResponse('%s注册成功' % uname)


def test_cors(request):
    return render(request, 'cross.html')


def cross_server(request):
    func = request.GET.get('callback')
    return HttpResponse(func + '("这是跨域的数据")')


def cross_server_json(request):
    func = request.GET.get('callback')
    dic1 = {'name':'tedu','age':18}
    # func + "('+dic1+')"
    # print("...")
    return HttpResponse(func + "("+json.dumps(dic1)+")")