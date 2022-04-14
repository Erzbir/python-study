def uio(num):
    num_l = str(num)
    length = len(num_l)
    lis_1 = []
    for a in range(1, length + 1):
        lis_1.append(int(num_l[a - 1:a]))
    num_s = 0
    for c in lis_1:
        num_s += c
    return num_s


def pan(num_i, num_s):
    if num_i // 11 == num_s:
        print(num_i)


for num_n in range(100, 1000):
    pan(num_n, uio(num_n))
