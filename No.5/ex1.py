def fibo(n):
    n_1 = 1
    n_2 = 1
    count = 2
    if n > 2:
        num = 2
        while count < n:
            num = n_2 + n_1
            n_2 = n_1
            n_1 = num
            count += 1
        print(num)
    if n == 1 or n == 2:
        print(n_1)


num_n = int(input("输入第几项:"))
fibo(num_n)
