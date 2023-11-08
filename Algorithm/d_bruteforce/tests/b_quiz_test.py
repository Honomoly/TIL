import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/d_bruteforce')
from b_quiz import *
import random

class QuizTest(unittest.TestCase):
    def test_dwarf(self):
        arr = [round(random.randrange(10,15)) for _ in range(7)]
        t = 100 - sum(arr)
        arr[6] = arr[6] + t
        
        arr.append(round(random.randrange(1,20)))
        arr.append(round(random.randrange(1,20)))
        print()
        print("Problem : ", arr)
        rlt = dwarf(arr)
        print(rlt, sum(rlt))
        