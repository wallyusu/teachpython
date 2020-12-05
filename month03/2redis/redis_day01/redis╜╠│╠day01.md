## ** Redis-day01-note**

**Redis介绍**

- **特点及优点**

```python
1、开源的，使用C编写，基于内存且支持持久化 # (sql是关系型，存储介质为硬盘，redis为KV型，存储介质是内存)
2、高性能的Key-Value的NoSQL数据库
3、支持数据类型丰富，字符串strings，散列hashes，列表lists，集合sets，有序集合sorted sets 等等
4、支持多种编程语言（C C++ Python Java PHP ... ）
5、单进程单线程
```

- **与其他数据库对比**

```python
1、MySQL : 关系型数据库，表格，基于磁盘，慢
2、MongoDB：键值对文档型数据库，值为类似JSON文档，数据结构相对单一
3、Redis的诞生是为了解决什么问题？？
   # 解决硬盘IO带来的性能瓶颈
```

- **应用场景**

```python
1，缓存
2，并发计数
	radis本身为单进程单线程，不会出现超买超卖现象
3，排行榜
	radis为有序集合
4，生产者消费者模型
	生产者将相关任务放入队列中，消费中从队列中获取任务。消费者为单独的线程或进程，来进行任务的耗时操作。引入生产消费者可以实现并发。
...
```

- **redis版本**

```python
1、最新版本：5.0
2、常用版本：2.4、2.6、2.8、3.0(里程碑)、3.2、3.4、4.0(教学环境版本)、5.0
```

- **Redis附加功能**

```python
1、持久化
  将内存中数据保存到磁盘中，保证数据安全，方便进行数据备份和恢复
2、过期键功能
   为键设置一个过期时间，让它在指定时间内自动删除
   <节省内存空间>
   # 音乐播放器，日播放排名，过期自动删除
3、事务功能
   原子的执行多个操作。# redis的事务功能比较弱，不具有原子性。
4、主从复制	# 主要解决单点失效问题，如数据分布在不同服务器上，如主服务器瘫痪，可以从从服务器上选择一个主服务器，一主多从。
5、Sentinel哨兵 # 当主服务器瘫痪，可以从服务器上选择一个主服务器，所有的操作都需要手动去操作。哨兵可以监控，监控多组redis服务的运行状态，自动化的进行部署。哨兵端口为：26379
```

## **安装**

- Ubuntu

```python
# 安装
sudo apt-get install redis-server
# 服务端启动
sudo /etc/init.d/redis-server status | start | stop | restart
# 客户端连接
redis-cli -h IP地址 -p 6379 -a 密码
```

## **配置文件详解**

- **配置文件所在路径**

```python
/etc/redis/redis.conf # 一般安装软件都在etc目录中
mysql的配置文件在哪里？ : /etc/mysql/mysql.conf.d/mysqld.cnf
```

- **设置连接密码**

```python
1、requirepass 密码 进入配置文件所在路径后，输入：500，将requirepass的# 去掉，后面加上密码,:wq退出
2、重启服务
   sudo /etc/init.d/redis-server restart
3、客户端连接
   redis-cli -h 127.0.0.1 -p 6379 -a 123456 # -h 本机 -p 端口 -a 密码 Sentinel哨兵端口为：26379
   127.0.0.1:6379>ping
    # 方法二
    redis-cli
    127.0.0.1:6379>auth 密码
```

- **允许远程连接**

```python
1、注释掉本地IP地址绑定
  69行: # bind 127.0.0.1 ::1
2、关闭保护模式(把yes改为no) # 不支持别的连接，即为保护模式
  88行: protected-mode no
3、重启服务
  sudo /etc/init.d/redis-server restart
```

- **通用命令 ==适用于所有数据类型==**

```python
# 切换库(number的值在0-15之间,db0 ~ db15)
select number
# 查看键,生产模式下，不要使用该命令
keys 表达式  # keys *
# 数据类型
type key
# 键是否存在
exists key
# 删除键
del key
# 键重命名
rename key newkey
# 清除当前库中所有数据（慎用），一般公司会将这两个命令禁掉！
flushdb
# 清除所有库中所有数据（慎用）
flushall
```



## 数据类型

### **字符串类型(string)**

- **特点**

```python
1、字符串、数字，都会转为字符串来存储，因为好显示，好操作。
2、以二进制的方式存储在内存中
```

- **字符串常用命令-==必须掌握==**

```python
# 1. 设置一个key-value
set key value
# 2. 获取key的值
get key
# 3. key不存在时再进行设置(nx)
set key value nx  # not exists
# 4. 设置过期时间(ex)
set key value ex seconds

# 5. 同时设置多个key-value
mset key1 value1 key2 value2 key3 value3
# 6. 同时获取多个key-value
mget key1 key2 key3 
```

- **字符串常用命令-==作为了解==**

```python
# 1.获取长度
strlen key
# 2.获取指定范围切片内容 [包含start stop]
getrange key start stop
# 3.从索引值开始，value替换原内容
setrange key index value
```

- **数值操作-==字符串类型数字(必须掌握)==**

```python
# 整数操作
incrby key 步长
decrby key 步长
incr key : +1操作
decr key : -1操作
# 应用场景: 抖音上有人关注你了，是不是可以用INCR呢，如果取消关注了是不是可以用DECR
# 浮点数操作: 自动先转为数字类型，然后再进行相加减，不能使用append
incrbyfloat key step
```

- **string命令汇总**

```python
# 字符串操作
1、set key value
2、set key value nx
3、get key
3、mset key1 value1 key2 value2
4、mget key1 key2 key3
5、set key value nx ex seconds
6、strlen key 
# 返回旧值并设置新值（如果键不存在，就创建并赋值）
7、getset key value
# 数字操作
7、incrby key 步长
8、decrby key 步长
9、incr key
10、decr key
11、incrbyfloat key number#(可为正数或负数,为float类型）

# 设置过期时间的两种方式
# 方式一
1、set key value ex 3
# 方式二
1、set key value
2、expire key 5 # 秒
3、pexpire key 5 # 毫秒
# 查看存活时间
ttl key # 如果设置了set key value ex 60秒后过期了，再次get name后 会自动被动删除。
# 删除过期
persist key
```

- **string数据类型注意**

```python
# key命名规范
可采用 - wang:email
# key命名原则
1、key值不宜过长，消耗内存，且在数据中查找这类键值的计算成本高
2、不宜过短，可读性较差
# 值
1、一个字符串类型的值最多能存储512M内容
```

- 业务场景
  - 缓存
    - 将mysql中的数据存储到redis字符串类型中
  - 并发计数 - 点赞/秒杀
    - 说明：通过redis单进程单线程的特点，由redis负责计数，并发问题转为串行问题
  - 带有效期的验证码  - 短信验证码
    - 借助过期时间，存放验证码；到期后，自动消亡

**练习**

```python
1、查看 db0 库中所有的键
127.0.0.1:6379> select 0
127.0.0.1:6379> keys *
2、设置键 trill:username 对应的值为 user001，并查看
127.0.0.1:6379> set trill:username user001
OK
127.0.0.1:6379> get trill:username
"user001"
3、获取 trill:username 值的长度
127.0.0.1:6379> strlen trill:username
(integer) 7
4、一次性设置 trill:password 、trill:gender、trill:fansnumber 并查看（值自定义）
127.0.0.1:6379> mset trill:password 123456 trill:gender m trill:fansnumber 1000
OK
127.0.0.1:6379> mget trill:password trill:gender trill:fansnumber
1) "123456"
2) "m"
3) "1000"
5、查看键 trill:score 是否存在
127.0.0.1:6379> exists trill:score
(integer) 0
6、增加10个粉丝
127.0.0.1:6379> incrby trill:fansnumber 10
(integer) 1010
7、增加2个粉丝（一个一个加）
127.0.0.1:6379> incr trill:fansnumber
(integer) 1011
127.0.0.1:6379> incr trill:fansnumber
(integer) 1012
8、有3个粉丝取消关注你了
127.0.0.1:6379> decrby trill:fansnumber 3
(integer) 1009
9、又有1个粉丝取消关注你了
127.0.0.1:6379> decr trill:fansnumber
(integer) 1008
10、思考、思考、思考...,清除当前库
127.0.0.1:6379> flushdb
OK
11、一万个思考之后，清除所有库
127.0.0.1:6379> flushall
OK
```

### **列表数据类型（List）**

- **特点**

```python
1、元素是字符串类型
2、列表头尾增删快，中间增删慢，增删元素是常态
3、元素可重复
4、最多可包含2^32 -1个元素
5、索引同python列表
6、常常将其当成队列使用。
```

- **列表常用命令**

```python
# 增	[左头右尾] [l左r右 一个个压入]
1、从列表头部压入元素
	LPUSH key value1 value2 
    返回：list长度
2、从列表尾部压入元素
	RPUSH key value1 value2
    返回：list长度
3、从列表src尾部弹出1个元素,压入到列表dst的头部
	RPOPLPUSH src dst
    返回：被弹出的元素
4、在列表指定元素后/前插入元素	[不推荐使用]
	LINSERT key after|before value newvalue
    返回：
		1，如果命令执行成功，返回列表的长度
		2，如果没有找到 pivot ，返回 -1
		3，如果 key 不存在或为空列表，返回 0 

# 查
5、查看列表中元素
	LRANGE key start stop
  # 查看列表中所有元素: LRANGE key 0 -1
6、获取列表长度
	LLEN key

# 删
7、从列表头部弹出1个元素
	LPOP key
8、从列表尾部弹出1个元素
	RPOP key
9、列表头部,阻塞弹出,列表为空时阻塞 (可通过timeout设置阻塞时间)
	BLPOP key timeout
10、列表尾部,阻塞弹出,列表为空时阻塞
	BRPOP key timeout
  # 关于BLPOP 和 BRPOP
  	1、如果弹出的列表不存在或者为空，就会阻塞
	2、超时时间设置为0，就是永久阻塞，直到有数据可以弹出
	3、如果多个客户端阻塞再同一个列表上，使用First In First Service原则，先到先服务
11、删除指定元素
	LREM key count value
    count>0：表示从头部开始向表尾搜索，移除与value相等的元素，数量为count （左头右尾）
	count<0：表示从尾部开始向表头搜索，移除与value相等的元素，数量为count
	count=0：移除表中所有与value相等的值
    返回：被移除元素的数量
    
12、保留指定范围内的元素
	LTRIM key start stop
    返回：ok
    样例：
  		LTRIM mylist1 0 2 # 只保留前3条
  		# 应用场景: 保存微博评论最后500条
  		LTRIM weibo:comments 0 499
# 改
13、将列表 key 下标为 index 的元素的值设置为 value
	LSET key index newvalue
```

**练习**

```python
1、查看所有的键
127.0.0.1:6379> keys *
1) "lk2"
2) "lk1"
2、向列表 spider:urls 中以RPUSH放入如下几个元素：01_baidu.com、02_taobao.com、03_sina.com、04_jd.com、05_xxx.com
127.0.0.1:6379> rpush spider:urls 01_baidu.com 02_taobao.com 03_sina.com 04_jd.com 05_xxx.com
(integer) 5
3、查看列表中所有元素
127.0.0.1:6379> lrange spider:urls 0 -1
1) "01_baidu.com"
2) "02_taobao.com"
3) "03_sina.com"
4) "04_jd.com"
5) "05_xxx.com"
4、查看列表长度
127.0.0.1:6379> llen spider:urls
(integer) 5
5、将列表中01_baidu.com 改为 01_tmall.com
127.0.0.1:6379> lset spider:urls 0 01_tmall.com
OK
6、在列表中04_jd.com之后再加1个元素 02_taobao.com
127.0.0.1:6379> linsert spider:urls after 04_jd.com 02_taobao.com
(integer) 6
7、弹出列表中的最后一个元素
127.0.0.1:6379> rpop spider:urls
"05_xxx.com"
8、删除列表中所有的 02_taobao.com
127.0.0.1:6379> lrem spider:urls 0 02_taobao.com
(integer) 2
9、剔除列表中的其他元素，只剩前3条
127.0.0.1:6379> ltrim spider:urls 0 2
OK
```

## **python交互redis**

- **模块(redis)**

Ubuntu 

```python
sudo pip3 install redis
```

- **使用流程**

```python
import redis
# 创建数据库连接对象
r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
```

- **通用命令代码示例**

```python
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
```

- **python操作list**

```python

```

**list案例: 一个进程负责生产任务，一个进程负责消费任务**

进程1: 生产者

```python
# 在2redis下创建productor.py:
import redis

r = redis.Redis(password='123456')

# 模拟，将任务放到队列中
# 任务类别_收件人_发件人_内容
task = '%s_%s_%s_%s'%('sendEmail','123@qq.com','456@163.com','hello world')
# 将任务发送到队列中
r.lpush('pylt1',task)
```

进程2: 消费者

```python
# 在2redis下创建consumer.py:
import redis
r = redis.Redis(password='123456')

while True:
    task = r.brpop('pylt1',10)  # (b'pylt1', b'sendEmail_123@qq.com_456@163.com_hello world')
    print(task)
    if task:
        task_data = task[1]
        task_str = task_data.decode()
        task_list = task_str.split('_')
        print('-收到任务，任务类型是：%s-'%task_list[0])
        # 执行发送邮件的任务...
    else:
        print('-no task!!!-')
```

- **python操作string**

```python

```

推荐书籍和软件：大话设计模式	 GOF 23中模式	rabbitMQ









