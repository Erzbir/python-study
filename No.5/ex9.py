a = '9.00我去bc上学'
b = []
count = 0
for i in range(len(a)):
    b.append(a[i])
for d in b:
    if d.isalpha():
        count += 1
print(count)
