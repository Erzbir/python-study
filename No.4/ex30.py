def uo(num):
    if num%3 != 0:
        return True
    else:
        return False


n = 0
for num in range(1,101):
    if uo(num):
        n+=num
print(n)