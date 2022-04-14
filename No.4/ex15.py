def niu(num):
    if num == 100:
        print("买车")
    elif num >= 90:
        print("买MP4")
    elif 60 <= num < 90:
        print("买书")
    elif num < 60:
        print("不买")


num_n = float(input("输入成绩:"))
niu(num_n)
