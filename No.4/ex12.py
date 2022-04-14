c = 0
b = ['1']
for a in range(1000, 10000):
    if a % 1000 // 100 == 3:
        if a % 1000 % 100 // 10 == 6:
            if a // 2 == a / 2:
                if a // 3 == a / 3:
                    b.append(a)
                    c += 1
print(f"最小数: {b[1]}   最小数: {b[c]}")
