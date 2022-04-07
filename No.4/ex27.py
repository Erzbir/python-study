import fractions
def fract(a,b):
        if a*b == 140:
            print(fractions.Fraction(a,b))


for a in range(1,141):
    for b in range(1,141):
        fract(a,b)