# 创建连接池并连接到redis
# 池化（pool）技术：可以预先创建几个连接或者需要时创建连接并放到连接池中，然后需要数据库连接时，直接从连接池中获取连接，不需要临时创建。当使用完后，不会关闭连接而是放回连接池，以备下一个客户端使用。以此带来的好处是，不需要频繁的创建和关闭连接，不会耗CPU。
# 类似的还有线程池。
import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6381)
r = redis.Redis(connection_pool=pool)


def withpipeline(r):
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i + 1
        p.set(key, value)
    p.execute()


def withoutpipeline(r):
    for i in range(1000):
        key = 'test2' + str(i)
        value = i + 1
        r.set(key, value)


# 使用流水线的时间消耗要小很多
if __name__ == '__main__':
    t1 = time.time()
    # 使用流水线的时间消耗：0.023
    # withpipeline(r)
    # 不使用流水线的时间消耗：0.057
    withoutpipeline(r)
    t2 = time.time()
    print('time is %s' % (t2 - t1))
