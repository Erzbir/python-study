def NarcNum(num):
    num_1 = num//100
    num_2 = num%100//10
    num_3 = num%100%10
    x = False
    if num_1**3+num_2**3+num_3**3 == num:
        x = True
    return x


for num in range(100,1000):
    a = NarcNum(num)
    if a:
        print(num)

