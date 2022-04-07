import random

x = random.randint(0, 100)


def caiquan(c, d):
    while True:
        global x
        if c < d & c <= 100:
            print("猜小了")
            print(x)
            break
        if c > d & c <= 100:
            print("猜大了")
            print(x)
            break
        if c == d & c <= 100:
            print("猜对了")
            x = random.randint(0, 100)
            break


while True:
    print("开始")
    a = int(input("输入101退出,输入一个数:"))
    if a > 100:
        print("退出程序")
        break
    caiquan(a,x)
