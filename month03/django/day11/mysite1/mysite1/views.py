from django.http import HttpResponse


def index_view(request):
    return HttpResponse('<h1>这是默认页面，怀念小火箭</h1>')


def page1_view(request):
    return HttpResponse('<h1>这是第一个页面</h1>')


def page2_view(request):
    return HttpResponse('<h1>这是第二个页面</h1>')


def pagen_view(request, num):
    return HttpResponse('<h1>这是第%s个页面</h1>' % num)


def page_str(request, info):
    return HttpResponse('info:%s' % info)


def page_op(request, a, op, b):
    r = 0
    if op == 'add':
        r = a + b
    elif op == 'sub':
        r = a - b
    elif op == 'mul':
        r = a * b
    else:
        return HttpResponse('op is wrong~')
    return HttpResponse('计算结果:%s' % r)


def birthday(request, y, m, d):
    return HttpResponse('生日：%s年%s月%s日' % (y, m, d))

def test_get(request):
    # http://127.0.0.1:5000/test_get
    # /test_get
    print(request.path_info)
    # GET
    print(request.method)
    # http://127.0.0.1:5000/test_get?a=100&b=200&c=300
    # <QueryDict: {'a': ['100'], 'b': ['200'], 'c': ['300']}>
    # 类字典结构，包含了查询字符串中的名称和值
    print(request.GET)

    # 包含了查询字符串的Path
    print(request.get_full_path())

    return HttpResponse('---text get---')
