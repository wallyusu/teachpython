saulschena = [1, 2, 4, 8, 11, 23, 111]
num = int(input('请输入数字:'))
# for i in range(len(saulschena)):
#     if num == saulschena[i]:
#         print(i)
#     if num not in saulschena:
#         print(-1)
#         break
#     else:
#         continue

for i,r in enumerate(saulschena):
    if num == r:
        print(i)
    if num not in saulschena:
        print(-1)
        break


