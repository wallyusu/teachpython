import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response


class MyMiddleWare2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法2 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法2 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法2 process_response 被调用")
        return response


class MyMw(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):
        # 获取远程ip
        cip = request.META['REMOTE_ADDR']
        if not re.match(r'^/test', request.path_info):
            return
        times = self.visit_times.get(cip, 0)
        if times >= 5:
            return HttpResponse('no way!')
        self.visit_times[cip] = times + 1
        print('%s visit we %s times' % (cip, self.visit_times[cip]))
