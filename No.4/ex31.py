def zhi(num):
    fg = True
    if num == 1:
        fg = False
    for a in range(2,num//2+1):
        if num%a == 0:
            fg = False
    return fg


N = int(input("输入一个正整数:"))
sum = 0
for a in range(1,N+1):
    if zhi(a):
        sum+=a
print(sum)