import redis

r = redis.Redis(password='123456')

r.zadd('z1', {'tedu': 1000, 'tedu2': 600})
r.zadd('z2', {'tedu2': 800, 'tedu3': 500})
print(r.zrange('z1', 0, -1, withscores=True))
print(r.zrange('z2', 0, -1, withscores=True))
# 并集，不带权重的
r.zunionstore('z3',['z1','z2'],aggregate='sum')  # 不带权重，内用列表
print(r.zrange('z3',0,-1,withscores=True))
# 并集，带权重的
r.zunionstore('z4',{'z1':0.2,'z2':0.8},aggregate='sum')  # 带权重，内用字典
print(r.zrange('z4',0,-1,withscores=True))

r.delete('z1')
r.delete('z2')
r.delete('z3')
r.delete('z4')