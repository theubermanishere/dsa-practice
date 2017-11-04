# Implementation of the Euclid's Algorithm for calculation the GCD of two numbers x,y.

def gcd(x,y):
    rem = 1
    while(rem != 0):
        if y > x:
            rem = y%x
            if rem == 0:
                return x
            y = y - x 
        else:
            rem = x%y
            if rem == 0:
                return y
            x = x - y


