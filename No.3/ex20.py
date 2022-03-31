from calendar import c


a = [1,213,122,11,1,23,1,3,3,3,4,5,6,7,8,8,8,8]
print(a)
print(set(a))
b = [1,1,1,1,1,2,2,2,3,3,3,4,4,4]
print(b)
c = {}.fromkeys(b).keys()
print(c)