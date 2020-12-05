from django.contrib import admin
from .models import *

# Register your models here.
# 模型管理器类
class PublisherManager(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id']
    search_fields = ['id','name']
    list_editable = ['name']


class BookManager(admin.ModelAdmin):
    list_display = ['id','title','publisher']
    list_filter = ['publisher']

admin.site.register(Publisher,PublisherManager)
admin.site.register(Book,BookManager)