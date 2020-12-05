import redis
r = redis.Redis(password='123456')
r.hset('pyh1','uname','tarena')
print(r.hget('pyh1', 'uname').decode())
r.hmset('pyh1',{'age':22,'desc':'it training'})
print(r.hmget('pyh1','uname','age'))
print(r.hgetall('pyh1'))
print(r.hkeys('pyh1'))
print(r.hvals('pyh1'))
# 操作后直接删除，避免因重复操作，产生垃圾数据
r.delete('pyh1')