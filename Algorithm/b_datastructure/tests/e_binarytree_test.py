import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from e_binarytree import *

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            self.tree.insert(i)
    
    def test_search1(self):
        print()
        print(self.tree.pre_order())
        print(self.tree.mid_order())
        print(self.tree.lat_order())
    
    def test_search2(self):
        print()
        print(self.tree.order_with_stack_fuk(-1))
        print(self.tree.order_with_stack_fuk(0))
        print(self.tree.order_with_stack_fuk(1))
    
    def test_search3(self):
        print()
        print(self.tree.pre_order_with_stack())
        print(self.tree.in_order_with_stack())
        print(self.tree.in_order_with_stack2())
        print(self.tree.post_order_with_stack())
        print(self.tree.post_order_with_stack2())
    
    def test_search4(self):
        print()
        self.tree.bfs()