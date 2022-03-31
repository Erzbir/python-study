import math
a = int(input("输入整数:"))
x = True
if a == 1:
    x = False
sqrt = int(math.sqrt(a))
for c in range(2, sqrt + 1):
    if  a % c == 0:
        x = False
        break
if x == False:
    print("不是质数")
else:
    print("是质数")