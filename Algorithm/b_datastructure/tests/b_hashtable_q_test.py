import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from b_hashtable_q import *

class HashQTest(unittest.TestCase):
    def test_q1(self):        
        texts = ['hashtable', 'samsung', 'aabb']
        print()
        for text in texts:
            print(q1(text))