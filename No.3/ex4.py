a = int(input("输入高度:"))
for c in range(0,a+1):
    print(" "*(a-c+1)+'* ' *(c-1))
for c in range(0,a):
    print(" "*(c+2)+'* ' *(a-c-2))