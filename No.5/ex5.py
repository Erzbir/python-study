def get_num(num):
    if num%5 == 0:
        if num%6 == 0:
            return 0
        else:
            print(num)
    if num%6 == 0:
        if num%5 == 0:
            return 0
        else:
            print(num)


for num in range(5,10001):
    get_num(num)