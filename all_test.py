import searching

class TestSearching(object):
    def test_binary1(self):
        assert searching.binary_search(searching.arr,5) == 5
    def test_binary2(self):
        assert searching.binary_search(searching.arr,11) == "Not-Found"
    def test_recursive1(self):
        assert searching.recursive_binary_search(searching.arr,0,len(searching.arr)-1,5) == 5
    def test_recursive2(self):
        assert searching.recursive_binary_search(searching.arr,0,len(searching.arr)-1,11) == "Not-Found"
