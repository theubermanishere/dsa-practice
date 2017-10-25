import searching
import sorting
import random

class TestSearching(object):
    def test_binary1(self):
        assert searching.binary_search(searching.arr,5) == 5
    def test_binary2(self):
        assert searching.binary_search(searching.arr,11) == "Not-Found"
    def test_recursive1(self):
        assert searching.recursive_binary_search(searching.arr,0,len(searching.arr)-1,5) == 5
    def test_recursive2(self):
        assert searching.recursive_binary_search(searching.arr,0,len(searching.arr)-1,11) == "Not-Found"

class TestSorting(object):
    def test_selection_sort(self):
        array = sorting.selection_sort(sorting.arr)
        for i in range(5):
            a = random.randint(0,len(array)-1)
            b = random.randint(0,len(array)-1)
            if (a > b):
                assert array[a] > array[b]
            elif (a <= b):
                assert array[a] <= array[b]
    def test_insertion_sort(self):
        array = sorting.insertion_sort(sorting.arr)
        for i in range(5):
            a = random.randint(0,len(array)-1)
            b = random.randint(0,len(array)-1)
            if (a > b):
                assert array[a] > array[b]
            elif (a <= b):
                assert array[a] <= array[b]
 
