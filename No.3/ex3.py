a = float(input("输入身高(m):"))
b = float(input("输入体重(kg):"))
BMI = b/(a**2)
if BMI < 18.5:
    print("过轻")
if 18.5 <= BMI < 24:
    print("正常")
if 24 <= BMI <27:
    print("过重")
if 27 <= BMI <30:
    print("轻度肥胖")
if 30 <= BMI <35:
    print("中度肥胖")
if BMI >= 35:
    print("重度肥胖")