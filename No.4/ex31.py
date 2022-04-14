def zhi(num):
    fg = True
    if num == 1:
        fg = False
    for b in range(2, num // 2 + 1):
        if num % b == 0:
            fg = False
    return fg


N = int(input("输入一个正整数:"))
sums = 0
for a in range(1, N + 1):
    if zhi(a):
        sums += a
print(sums)
