from django.contrib import admin
from .models import Book

# Register your models here.
# 模型管理器类
class BookManager(admin.ModelAdmin):
    # 以列表形式排列
    list_display = ['id','title','pub','price','market_price']
    # 对字段设置超链接可选
    list_display_links = ['id','title','pub']
    # 过滤器
    list_filter = ['pub']
    # 更改列表页面上的搜索框
    search_fields = ['id','title']
    # 可直接在列表中修改值
    list_editable = ['market_price']
admin.site.register(Book,BookManager)