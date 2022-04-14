def pio(num):
    num_s = str(num)
    length = len(num_s)
    num_list = []
    for a in range(1, length + 1):
        num_p = num_s[a - 1:a]
        num_list.append(num_p)
    return num_list


def comb(list_comb):
    x = ''
    for a in list_comb:
        x += a
    return int(x)


for x in range(10000, 100001):
    list_1 = pio(x)
    list_1.insert(0, '7')
    num_1 = comb(list_1)
    list_2 = pio(x)
    list_2.append('7')
    num_2 = comb(list_2)
    if num_1 / num_2 == 5:
        print(x)
        break
