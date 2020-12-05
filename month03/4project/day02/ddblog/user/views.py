import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user.models import UserProfile
import hashlib
import time  # 设置过期时间导入的包
import jwt  # 设置共享秘钥导入的包
from django.conf import settings

# Create your views here.
from django.views import View


class UsersView(View):
    def get(self, request, username=None):
        if username:
            # 返回单个用户信息
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                print('-get user error is %s-' % e)
                result = {'code': 10104, 'error': '该用户不存在'}
                return JsonResponse(result)
            # 根据查询字符串获取指定数据
            keys = request.GET.keys()
            if keys:
                data = {}
                for k in keys:
                    if k == 'password':
                        continue
                    if hasattr(user, k):
                        data[k] = getattr(user, k)
                result = {'code': 200, 'username': username, 'data': data}
            else:
                # 获取用户的全量数据
                result = {'code': 200, 'username': username,
                          'data': {'info': user.info, 'sign': user.sign, 'nickname': user.nickname,
                                   'avatar': str(user.avatar)}}
            return JsonResponse(result)
        else:
            # 返回所有用户信息
            pass
        return HttpResponse('--users get--')

    def post(self, request):
        json_str = request.body  # 获取json串
        json_obj = json.loads(json_str)  # 反序列化 将json串转换为对象
        username = json_obj['username']  # 一个个字段通过键拿值
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        print(username, email, phone, password_1, password_2)
        # 1 用户名长度检查
        if len(username) > 11:
            result = {'code': 10100, 'error': '用户名太长'}
            return JsonResponse(result)  # JsonResponse 会自动返回为json串
        # 2 检查用户名是否可用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10101, 'error': '用户名已被占用'}
            return JsonResponse(result)
        # 3 两次密码要一致
        if password_1 != password_2:
            result = {'code0': 10102, 'error': '两次密码不一致'}
            return JsonResponse(result)
        # 4 hash处理
        md5 = hashlib.md5()
        md5.update(password_1.encode())  # 添加欲hash的内容，类型为 bytes
        password_h = md5.hexdigest()  # 返回摘要，作为十六进制数据字符串值
        # 5 添加到数据库
        try:  # 使用try为了防止几个客户同时注册提交时账号一致报错
            user = UserProfile.objects.create(username=username,
                                              password=password_h,
                                              email=email,
                                              phone=phone,
                                              nickname=username)
        except Exception as e:
            print('create error is %s' % e)
            result = {'code': 10103, 'error': '用户名被占用'}
            return JsonResponse(result)
        # 签发token 生成token后，保存到客户端的本地存储中。本地存储的数据不会自动提交，需要时，通过代码提交。
        token = make_token(username)
        # 字节串表示的token转换为字符串
        token = token.decode()
        # res.data.token
        return JsonResponse({'code': 200, 'username': username, 'data': {'token': token}})


def make_token(username, expire=3600 * 24):  # expire过期时间，设置token用户验证时效
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    return jwt.encode(payload, key, algorithm='HS256')
    # pyjwt方法 encode(payload, key, algorithm) 自动拼接,同base64(header) + '.' + base64(payload) + '.' +  base64(sign)
