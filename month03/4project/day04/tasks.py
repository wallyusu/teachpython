from celery import Celery
import time

# 1. 创建Celery对象，并配置broker(消息队列)
app = Celery('demo1',
             broker='redis://@127.0.0.1:6379/1')
# /1为1库，0库后面什么都不用写  如有密码，为：redis://:123456(密码)@127.0.0.1:6379/1 用于存放任务消息的配置


# 2. 创建任务函数
@app.task  # 添加装饰器，此函数才是任务函数，否则就是一般函数
def task_test():
    print('task is running...')
    time.sleep(10)
    print('task is finish.')
