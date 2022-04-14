import math


def san(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    l = a + b + c
    print(f"面积={s}\n周长={l}")


num_1 = float(input("输入三角形的第一条边长:"))
num_2 = float(input("输入三角形的第二条边长:"))
num_3 = float(input("输入三角形的第三条边长:"))
