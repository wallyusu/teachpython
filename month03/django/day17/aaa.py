# l = [0,1,2]
# x = 0
# x,l[x] = 1,5
# print(l)

x = [1,2]
y = [1,2]  # false id的地址不同 140635244799304 140635244799880

x = 1
y = 1

x = '12'
y = '12'
print(x is y)
print(id(x), id(y))