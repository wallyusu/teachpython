import redis

r = redis.Redis(password='123456')

# 模拟，将任务放到队列中
# 任务类别_收件人_发件人_内容
task = '%s_%s_%s_%s'%('sendEmail','123@qq.com','456@163.com','hello world')
# 将任务发送到队列中
r.lpush('pylt1',task)