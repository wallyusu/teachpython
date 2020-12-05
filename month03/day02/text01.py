import turtle
all = [] #创建一个空列表
for i in range(6): #用循环创建 6 个海龟，之后把海龟放入列表中
 t = turtle.Pen()
 t.shape("turtle")
 t.speed(0)
 t.lt(60*i) #让 6 个小海龟在生成之后就马上转到对应的方向
 all.append(t) #把小海龟放入列表
for k in range(200):
    for x in all: #遍历列表，把 x 变成列表里面的每一个小海龟，然后让每个小海龟都去移动
        x.fd(3)