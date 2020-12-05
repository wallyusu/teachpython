from celery import Celery
from django.conf import settings
import os

# 1. 为celery设置环境变量，告诉Celery为谁服务(Django)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_celery.settings')

# 2. 创建Celery对象
app = Celery('test_celery')

# 3. 配置app
app.conf.update(BROKER_URL='redis://@127.0.0.1:6379/1')  # 消息队列

# 4. 设置app自动加载任务(在项目中的各个子应用中查找)
app.autodiscover_tasks(settings.INSTALLED_APPS)
