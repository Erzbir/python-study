def fox(x):
    y = True
    if x == 1:
        y = False
    for a in range(2,x//2+1):
        if x%a == 0:
            y = False
            break
    return y


for num in range(50,151):
    a=fox(num)
    if a:
        print(num)
  