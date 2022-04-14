num = int(input("输入一个数:"))
if num & 1 == 0:
    print("是偶数")
    for num_1 in range(1, num + 1):
        if num_1 // 3 == num_1 / 3:
            print(num_1)
else:
    print("是奇数")
    for num_1 in range(1, num + 1):
        if num_1 // 5 == num_1 / 5:
            print(num_1)
