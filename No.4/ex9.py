def inal(a):
    x = True
    if a == 1:
        x = False
    for c in range(2, a // 2 + 1):
        if a % c == 0:
            x = False
            break
    if not x:
        print("不是质数")
    else:
        print("是质数")


b = int(input("输入整数:"))
inal(b)
