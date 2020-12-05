import html

from aptdaemon import console
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Note

def login_check(fn):
    def wrap(request,*args,**kwargs):
        # print('aaaaa:{}'.format(request.session['uname'], request.session['uid']))
        if 'uname' not in request.session or 'uid' not in request.session:
            c_uname = request.COOKIES.get('uname')
            c_uid = request.COOKIES.get('uid')
            if not c_uname or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['uname'] = c_uname
                request.session['uid'] = c_uid
                # session没有数据，cookie中有数据，可以继续...
        # session有数据，可以继续...
        return fn(request,*args,**kwargs)
    return wrap
# Create your views here.
# 只有登录用户才可以操作
@login_check
def add_view(request):
    if request.method == 'GET':
        return render(request,'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 转义：在Django模板中不需要，但是以后的项目大部分都是前后端分离的，所以那是需要转义
        title = html.escape(title)
        # session中一定有uid
        uid = request.session['uid']
        Note.objects.create(title=title,content=content,user_id=uid)
        return HttpResponse('添加笔记成功！')
