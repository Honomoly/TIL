import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/b_datastructure')
from a_list_q import *

class ListTest(unittest.TestCase):
    def test_q1(self):        
        texts = ['tomato', '토마토', '기러기' ,'Wild goose', '역삼역', 'Yeoksam station']
        for text in texts:
            if(check_palindrome(text)):
                print(text + ' 는 회문입니다.')