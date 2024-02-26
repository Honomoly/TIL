import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from b_hashtable import *

class HashTest(unittest.TestCase):
    def setUp(self):
        print()
        self.table = HashTable(4)
        self.table.add("a", "11")
        self.table.add("b", "22")
        self.table.add("c", "33")
        self.table.add("d", "44")
        self.table.add("e", "55")
        self.table.add("f", "66")
        self.table["a"] = "77"
        self.table.add("b", "88") # 오류
        self.table["g"] = "99" # 오류

    def test_hash(self):
        print(self.table)
        print(self.table["a"])
        print(self.table["g"]) # None
        print(self.table["e"])
        print("-------")
        for e in self.table:
            print(e)
        print("-------")
        del self.table["e"]
        print(self.table)