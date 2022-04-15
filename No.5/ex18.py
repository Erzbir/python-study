a = '我是学生一二三学生'
i = -1
a = list(a)
for j in a:
    i += 1
    if a[i] == '学' and a[i + 1] == '生':
        a[i] = 'x'
        a[i + 1] = 'x'
for c in a:
    print(c, end='')
