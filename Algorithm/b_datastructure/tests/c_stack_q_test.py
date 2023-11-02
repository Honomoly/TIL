import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from c_stack_q import *

class StackQTest(unittest.TestCase):
    def test_q1(self):
        self.assertTrue(is_pair('{}()[]'))  # True
        self.assertTrue(is_pair('{([])}'))  # True
        self.assertFalse(is_pair('{([}])}')) # False