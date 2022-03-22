x=input("输入1取余,2位运算")
a=int(input("输入整数:"))
if x=='1':
    print("取余")
    if a%2==0:
        print("为偶数")
    else:
        print("为奇数")
if x=='2':
    print("位运算")
    if a-1&a==a-1:
        print("为奇数")
    else:
        print("为偶数")