import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from c_stack import *

class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push("e")
        self.stack.push("4")
        self.stack.push("7")
        self.stack.push("k")
    
    def test_stack(self):
        print()
        print(self.stack)
        self.stack.pop()
        print(self.stack)
        print(self.stack.peek())