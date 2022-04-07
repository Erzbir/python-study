a = int(input("输入高度:"))
for c in range(1, a + 1):
    print(" " * (a - c) + '* ' * c)
