while True:
    a=int(input("输入一个整数:"))
    b=int(input("输入一个整数:"))
    print(a,b)
    a=a^b
    b=a^b
    a=a^b
    print(a,b)