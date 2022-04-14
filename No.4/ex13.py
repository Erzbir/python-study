for num in range(1000, 9999):
    num_1 = num // 1000
    num_2 = num % 1000 // 100
    num_3 = num % 1000 % 100 // 10
    num_4 = num % 1000 % 100 % 10
    if num * num_1 == num_4 * 1000 + num_3 * 100 + num_2 * 10 + num_1:
        print(num)
