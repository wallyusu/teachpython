from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html = '''
<form method='post' action="/test_get_post">
    姓名:<input type="text" name="username">
    <input type='submit' value='登录'>
</form>
'''


def test_get_post(request):
    if request.method == 'GET':
        # print(request.GET.get('a',100))
        print(request.GET.getlist('a'))  # ['100', '200', '300']
        # print(request.GET.get('username'))
        return HttpResponse(html)
    elif request.method == 'POST':
        # username = request.POST['username']
        username = request.POST.get('username')
        age = request.POST.get('age', 18)
        return HttpResponse('北京欢迎你：%s %s' % (username, age))


def birthday(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    return HttpResponse('生日为：%s年%s月%s日' % (year, month, day))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return '我叫%s,今年%s岁了' % (self.name, self.age)


def hello():
    return 'Hello Django'


def test_html(request):
    # 方式一
    # # 1.加载模板
    # t = loader.get_template('test_html.html')
    # # 2.将模板文件转换成字符串（包含字典数据）
    # html = t.render()
    # # 3.将字符串作为响应对象的参数
    # return HttpResponse(html)

    # 方式二
    # person = Person('宋小宝', 50)
    # d = {}
    # d['name'] = 'tedu'
    # d['age'] = 18
    # d['hobby'] = ['吃饭', '睡觉', '打豆豆']
    # d['score'] = {'语文': 99, '数学': 100, '英语': 100}
    # d['person'] = person
    # d['func1'] = hello
    # 字典数据没有可以不写
    # return render(request, 'test_html.html', d)

    # 方式三
    person = Person('宋小宝', 50)
    name = 'tedu'
    age = 18
    hobby = ['吃饭', '睡觉', '打豆豆']
    score = {'语文': 99, '数学': 100, '英语': 100}
    person = person
    func1 = hello
    script = '<script>alert(11111)</script>'

    list1 = ['关羽','张飞','赵云','马超','黄忠']
    list1 = []
    return render(request, 'test_html.html', locals())


def mycal_view(request):
    if request.method == 'GET':
        return render(request, 'mycalc.html')
    elif request.method == 'POST':
        # 1.获取数据
        x = request.POST.get('x')
        y = request.POST.get('y')
        op = request.POST.get('op')
        # 2.为空判断
        if not x or not y:
            return HttpResponse('请输入数据')
        # 3.类型转换,try
        try:
            x = int(x)
            y = int(y)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('请输入数值')

        # 4.通过不同的条件(操作符),运算得到结果
        if op == 'add':
            total = x + y
        elif op == 'sub':
            total = x - y
        elif op == 'mul':
            total = x * y
        elif op == 'div':
            total = x / y
        # 在模板页显示结果 render(...,...,local())
        return render(request, 'mycalc.html', locals())
        # 修改模板页
