def bmi_count(high, weight):
    bmi = weight / (high ** 2)
    if bmi < 18.5:
        print("过轻")
    elif 18.5 <= bmi < 24:
        print("正常")
    elif 24 <= bmi < 27:
        print("过重")
    elif 27 <= bmi < 30:
        print("轻度肥胖")
    elif 30 <= bmi < 35:
        print("中度肥胖")
    elif bmi >= 35:
        print("重度肥胖")


a = float(input("输入身高(m):"))
b = float(input("输入体重(kg):"))
bmi_count(a,b)
