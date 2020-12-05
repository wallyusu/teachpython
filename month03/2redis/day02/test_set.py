import redis

r = redis.Redis(password='123456')

# '武将':'张飞','周瑜','赵云','马超'
# '文臣':'司马懿','诸葛亮','周瑜','荀彧'
# 纯武将、纯文臣、文武双全、文臣武将
# lst = []
r.sadd('武将', '张飞', '周瑜', '赵云', '马超')
r.sadd('文臣', '司马懿', '诸葛亮', '周瑜', '荀彧')
# 纯武将
result = [i.decode() for i in r.sdiff('武将', '文臣')]
print(result)
r.delete('武将', '文臣')

# 纯文臣
result = [i.decode() for i in r.sdiff('文臣', '武将')]
print(result)
r.delete('武将', '文臣')

# 文武双全
result = [i.decode() for i in r.sinter('武将', '文臣')]
print(result)
r.delete('武将', '文臣')

# 文臣武将
result = [i.decode() for i in r.sunion('武将','文臣')]
print(result)
r.delete('武将','文臣')
