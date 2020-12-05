"""ddblog URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from user import views as user_views  # 对views模块的重命名
from btoken import views as btoken_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_cors', views.test_cors),
    path('test_cors_server', views.test_cors_server),
    # CBV 基于视图类
    path('v1/users', user_views.UsersView.as_view()),  # UsersView为类 .as_view()为类方法  user_views是对views模块的重命名
    path('v1/users/',include('user.urls')),
    path('v1/tokens',btoken_views.TokenView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)