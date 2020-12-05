from celery import Celery
import time

# 1. 创建并配置celery
app = Celery('demo2',
             broker='redis://@127.0.0.1:6379/1',
             backend='redis://@127.0.0.1:6379/2')

# 2.创建任务函数（消费者函数）
@app.task
def tasks_test(a, b):
    print('tasks is running...')
    time.sleep(10)
    return a * b
