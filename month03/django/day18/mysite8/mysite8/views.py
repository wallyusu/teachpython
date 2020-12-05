import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from test_upload.models import Content

# 文件下载
def test_csv(request):
    # 1. 指定响应内容的类型
    response = HttpResponse(content_type='text/csv')
    # 2. 指定以附件的形式，另存为...
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    # 3. 创建一个CSV的写入器，将内容写到response
    writer = csv.writer(response)
    writer.writerow(['编号', '名称'])
    books = [{'id': 1, 'name': 'python'},
             {'id': 2, 'name': 'c++'},
             {'id': 3, 'name': 'java'}
             ]
    for b in books:
        writer.writerow([b['id'],b['name']])
    return response

# 文件上传
@csrf_exempt  # 获取豁免保护 让所有文件都能上传
def test_upload(request):
    if request.method == 'GET':
        return render(request,'test_upload.html')
    elif request.method == 'POST':
        title = request.POST['title']
        afile = request.FILES['myfile']
        # 方式一、python的方式
        # 生成一个服务器端的文件存储路径
        # filename = os.path.join(settings.MEDIA_ROOT,afile.name)
        # with open(filename,'wb') as f:
        #     data = afile.file.read()
        #     f.write(data)
        # 方式二、Django的方式或者叫orm的方式[推荐]
        Content.objects.create(title=title,myfile=afile)
        return HttpResponse(f'上传文件成功!文件名称：{afile.name},文件标题：{title}')