def uio(num):
    num_l = str(num)
    length = len(num_l)
    lis_1=[]
    for a in range(1,length+1):
        lis_1.append(int(num_l[a-1:a]))
    num_s = 0
    for c in lis_1:
        num_s+=c
    return num_s
def pan(num,num_s):
    if num//11 == num_s:
        print(num)
for num in range(100,1000):
    pan(num,uio(num))
