a = [1,2,3,4,1231,5,6,7,8,9]
sum=0
av=0
min=0
max=0
for c in a:
    sum=sum+c
a.sort()
print(f"最大值:{a[len(a)-1]}")
print(f"最小值:{a[0]}")
av = sum/len(a)
print(f"平均值:{av}")
print(f"和:{sum}")