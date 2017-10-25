# Implementation of binary search

from math import floor

arr = list(i for i in range(0,10))

def binary_search(array,x):
    p = 0
    r = len(array) - 1
    while( p <= r):
        q = int(floor((p+r)/2))
        if (array[q] == x):
            return q
        elif (array[q] > x):
            r = q - 1
        else:
            p = q + 1
    return "Not-Found"

