# implementation of different sorting algorithms

import random

# Initialize a random array

arr = list()

for i in range(20):
    arr.append(random.randint(0,30))

def selection_sort(array):
    """ Implementation of selection sort.
    Takes only the array as input."""
    n = len(array)
    for i in range(n):
        smallest = i
        for j in range(i,n):
            if array[smallest] > array[j]:
                smallest = j
        temp = array[i]
        array[i] = array[smallest]
        array[smallest] = temp
    return array

def insertion_sort(array):
    """ Implementaiton of insertion sort."""
    n = len(array)
    for i in range(1,n):
        key = array[i]
        j = i-1
        while (j >= 0 and array[j] > key):
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

def merge_sort(array,p,r):
    """ Implementation of merge sort."""
    if (p >= r):
        return array
    q = floor((p+r)/2)
    merge_sort(array,p,q)
    merge_sort(array,q+1,r)
    merge(array,p,q,r)

