import redis

# 创建redis对象，连接之前，确定连接哪个库，进入之后不能修改。
# r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
r = redis.Redis(password='123456')  # 本地的服务，并且默认使用0库的话，可以采用缺省值,只使用密码 或 ()内什么都不写。
# 1.遍历所有的键
key_list = r.keys('*')
# 从函数中拿到的结果一般是字节串。
print(key_list)  # [b'lk2', b'lk1', b'spider:urls']
print(r.exists('k1'))
print(r.exists('lk1'))
# 2 输出键的类型，并将字节串结果转换为字符串
print(r.type('lk1').decode())
# 3 设置/获取
r.set('name', 'tedu', 100)
print(r.get('name').decode())  # tedu
# 4 设置获取多个值
r.mset({'a': 100, 'b': 200, 'c': 300})
print(r.mget('a', 'b', 'c'))
# 5 列表操作
# 5.1 从头部添加
r.delete('pyl1')
r.lpush('pyl1', 'a', 'b', 'c', 'd', 'e')
# 5.2 遍历
print(r.lrange('pyl1', 0, -1))
# 5.3 从列表的尾部中弹出元素
r.rpop('pyl1')  # 从尾部弹出一个元素
print(r.lrange('pyl1', 0, -1))
