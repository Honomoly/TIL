import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from d_queue_q import *

class QueueQTest(unittest.TestCase):
    def test_q1(self):
        print()
        print(q1(7))
        print(q1(10))
    
    def test_q2(self):
        print()
        print(q2(7, 3))
        print(q2(41, 2))