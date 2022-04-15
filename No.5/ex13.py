a = input("输入日期:")


def cha(x):
    for i in x:
        if not i.isdigit():
            return i


def tran(f):
    c = cha(f)
    f = f.split(c)
    i = 0
    q = ['1', '2', '3']
    print(f)
    for g in f:
        q[i] = g
        i += 1
    print('-'.join([q[0], q[1], q[2]]))


tran(a)
