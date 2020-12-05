from django.http import HttpResponse
from django.shortcuts import render
from .tasks import task_test
import datetime

# Create your views here.
# 生产者
def test_celery(request):
    task_test.delay()  # 放入消息队列
    now = datetime.datetime.now()
    html = 'result at %s'%(now.strftime('%H:%M:%S'))
    return HttpResponse(html)