import math
num_1 = float(input("输入三角形的第一条边长:"))
num_2 = float(input("输入三角形的第二条边长:"))
num_3 = float(input("输入三角形的第三条边长:"))
p = (num_2+num_1+num_3)/2
s = math.sqrt(p*(p-num_1)*(p-num_2)*(p-num_3))
l = num_1+num_2+num_3
print(f"面积={s}\n周长={l}")