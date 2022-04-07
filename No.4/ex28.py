def quotient(x):
    a = False
    if (80//x)%7 == 0 and x%2 == 1 and x%3 == 1 and x%4 == 1 and x%5 == 1 and x%6 == 1:
        a = True   
    return a


num = 1
while True:
    if quotient(num):
        print(num)
    num+=1
    if num == 10000:
        break

    