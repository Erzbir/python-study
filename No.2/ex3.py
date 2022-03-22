while True:
    a=float(input("输入成绩"))
    if a>100:
        print("不合法")
    if a==100:
        print("满分")
    if 90<=a<100:
        print("优秀")
    if 80<=a<90:
        print("良好")
    if 70<=a<80:
        print("还行")
    if 60<=a<70:
        print("及格")
    if 0<a<60:
        print("不及格")
    if a==0:
        print("退学")