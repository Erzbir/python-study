import math

d = input("任意键进入,out退出:")


def jisuan(a, b, c):
    if c == '*':
        print(f"{a} * {b} = {a * b}")
    if c == '/':
        print(f"{a} / {b} = {a / b}")
    if c == '+':
        print(f"{a} + {b} = {a + b}")
    if c == '-':
        print(f"{a} - {b} = {a - b}")
    if c == '//':
        print(f"{a} // {b} = {a // b}")
    if c == '%':
        print(f"{a} % {b} = {a % b}")
    if c == '**':
        print(f"{a} ^ {b} = {a ** b}")


while d != 'out':
    a = int(input("输入一个数:"))
    b = int(input("输入另一个数:"))
    c = input("输入运算符:")
    jisuan(a, b, c)
    d = input("任意键,输入out退出:")
