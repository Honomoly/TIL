import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from a_list import *

class ListTest(unittest.TestCase):
    def setUp(self):
        self.a = LinkedList()
        self.a.append("s")
        self.a.append("4")
        self.a.append("t")
        self.a.prepand("k")
        self.a.prepand("x")
    
    def test_list(self):
        print(self.a) # __str__() 호출
        print(len(self.a)) # __len__() 호출
        for i in self.a: # __iter__()및 __next__() 호출
            print(i, end="")
        print()
        print(self.a.pop())
        print(self.a)
        print(self.a[2]) # __getitem__() 호출
        self.a[2] = "e" # __setitem__() 호출
        print(self.a)
        del self.a[2] # __delitem__() 호출
        print(self.a)
        self.a.insert(2, "e")
        print(self.a)

if __name__ == "__main__":
    unittest.main()