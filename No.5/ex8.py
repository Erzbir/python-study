a = "user/rz/a.app"
a = a.split("/")
a[2] = a[2].split(".")
c = a[0] + '/' + a[1]
print(c)
for d in a[2]:
    print(d)
