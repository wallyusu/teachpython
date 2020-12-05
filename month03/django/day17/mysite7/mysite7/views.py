import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(15)  # 单位s
def test_cache(request):
    t1 = time.time()
    # time.sleep(3)
    return HttpResponse('t1 is %s' % t1)

def test_mw(request):
    print('--mw view in--')
    return HttpResponse('my mw view')
# 抵制CSRF攻击
def test_csrf(request):
    if request.method == 'GET':
        return render(request,'test_csrf.html')
    elif request.method == 'POST':
        username = request.POST['username']
        return HttpResponse('username is %s'% username)
# 分页函数
def test_page(request):
    list1 = ['a','b','c','d','e']
    # 创建分页器
    paginator = Paginator(list1,2)  # 每页显示2条列表内容
    cur_page = request.GET.get('page',1)  # 获取当前页面页码，默认值为第1页
    page = paginator.page(cur_page)  # 显示页码，有默认值1显示第一页
    return render(request,'test_page.html',locals())