def ksw(a):
    if 3 <= a <= 4:
        print("春季")
    if 5 <= a <= 8:
        print("夏季")
    if 9 <= a <= 10:
        print("秋季")
    if 11 <= a <= 12 or 1 <= a <= 2:
        print("冬季")


num = int(input("输入一个数:"))
ksw(num)
