def rabbit(n):
    rabb = 1
    count = 2
    if n > 0:
        if n <= 4:
            print(rabb)
        elif 4 < n <= 8:
            for a in range(1,n-3):
                rabb += 1
            print(rabb)
        else:
            rabb = 5
            for a in range(1,n-7):
                rabb = rabb+count
                count = count+1
            print(rabb)
n = int(input("输入天数:"))
rabbit(n)