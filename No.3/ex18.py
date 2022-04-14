def coin(a):
    b = [1]
    for e in range(2, a + 1):
        b.append(e)
    return b


coin_1 = coin(10)
coin_2 = coin(8)
coin_3 = coin(5)
coin_4 = coin(3)
coin_5 = coin(27)
coin_6 = coin(99)
num = 0
i = 0
coins = [coin_1, coin_2, coin_3, coin_4, coin_5, coin_6]
for c in coins:
    for d in c:
        num += 0.5
        i += 1
if i & 1 != 0:
    num += 1
print(int(num))
