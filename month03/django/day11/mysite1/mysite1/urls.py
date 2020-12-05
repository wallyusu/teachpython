"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns = [
    # 参数1是url，参数2是视图函数（分布式路由模块）
    path('admin/', admin.site.urls),
    path('',views.index_view),
    # 127.0.0.1:8000/page/1
    path('page/1',views.page1_view),
    path('page/2',views.page2_view),
    path('page/<int:num>',views.pagen_view),
    path('page/<str:info>',views.page_str),
    path('<int:a>/<str:op>/<int:b>',views.page_op),
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$',views.birthday),
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$',views.birthday),
    path('test_get',views.test_get),
]
