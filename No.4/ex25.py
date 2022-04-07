num = int(input("输入一个大于9的数"))


def pio(num):
    num_s = str(num)
    length = len(num_s)
    num_list=[]
    for a in range(1,length+1):
        num_p = int(num_s[a-1:a])
        num_list.append(num_p)
    return num_list


def comb(list):
    num=0
    for a in list:
        num+=a
    return num


list_1 = pio(num)
add_1 = comb(list_1)
if (num-add_1)%9 == 0 and num > 9:
     print("可以被整除")
else:
     print("不可以被整除")