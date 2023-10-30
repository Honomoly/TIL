import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/a_basic')
from c_math import *

class MathTest(unittest.TestCase):
    # def test_gcd(self):
    #     # print(gcd1(1022529, 517968))
    #     print(gcd2(1022529, 517968))
    #     print(lcm(1022529, 517968))
    
    def test_factorial(self):
        print(factorial1(10))
    
    def test_fibonacci(self):
        print(fibonacci1(40))
        print(fibonacci2(40))

if __name__ == "__main__":
    unittest.main()