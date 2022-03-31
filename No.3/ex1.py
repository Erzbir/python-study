import random
x = random.randint(0,100)
while True:
    a = input("输入任意键进入out退出:")
    if a == 'out':
        break
    print("开始")
    while True:
        a = int(input("输入101退出,输入一个数:"))
        if a < x & a <= 100:
            print("猜小了")
        if a > x & a <= 100:
            print("猜大了")
        if a == x & a <= 100:
            print("猜对了")
            x = random.randint(0,100)
            break
        if a > 100:
            print("退出程序")
            break