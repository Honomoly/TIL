import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from d_queue import *

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        for i in range(10):
            self.queue.enqueue(i)
    
    def test_queue(self):
        for i in range(10):
            print(self.queue.dequeue())
        print(self.queue.is_empty())