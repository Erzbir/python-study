from fractions import Fraction


def zhi(num):
    fg = True
    if num % 2 != 0:
        fg = True
    else:
        fg = False
    return fg


c = 1
pi = 0
pi_1 = 0
pi_2 = 0
for a in range(1, 100000):
    if zhi(a):
        if c == 1:
            pi_1 = Fraction(1, a)
            pi = pi + pi_1
        if c == -1:
            pi_2 = -Fraction(1, a)
            pi = pi + pi_2
        c = -c

print(float(4 * pi))
