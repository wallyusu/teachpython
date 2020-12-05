from django.urls import path
from . import views

# 代码自上而下运行，故v1/users/sms需放在最上面，如放在下方，当有Url后面为sms时，则默认判定为sms的用户了，与sms模块有重叠
# 且不能有叫sms的用户名
urlpatterns = [
    # http://127.0.0.1:8000/v1/users/sms
    path('sms', views.sms_view),
    # http://127.0.0.1:8000/v1/users/tedu
    path('<str:username>', views.UsersView.as_view()),
    # http://127.0.0.1:8000/v1/users/tedu/avatar
    path('<str:username>/avatar', views.user_avatar),
]
