from django.contrib import admin
from .models import Author
# Register your models here.
# 模型管理器类
class AuthorManager(admin.ModelAdmin):
    # 以列表形式排列
    list_display = ['id','name']
    # 对字段设置超链接可选
    list_display_links = ['id']
    # 过滤器
    list_filter = ['name']
    # 更改列表页面上的搜索框
    search_fields = ['id','name']
    # 可直接在列表中修改值
    list_editable = ['name']
admin.site.register(Author,AuthorManager)