import unittest
import sys
sys.path.append(r'/Users/jangseungheon/TIL/Algorithm/d_bruteforce')
from a_sort import *
import random

class SortTest(unittest.TestCase):
    def setUp(self):
        self.arr = [random.randrange(3000) for i in range(3000)]

    def test_bubble_sort1(self):
        print()
        if is_sorted(bubble_sort1(self.arr)):
            print("1. Sorted")
        else:
            print("1. Failed")
    
    def test_bubble_sort2(self):
        print()
        if is_sorted(bubble_sort2(self.arr)):
            print("2. Sorted")
        else:
            print("2. Failed")

    def test_bubble_sort3(self):
        print()
        if is_sorted(bubble_sort3(self.arr)):
            print("3. Sorted")
        else:
            print("3. Failed")
    
    def test_selection_sort(self):
        print()
        if is_sorted(selection_sort(self.arr)):
            print("1. Sorted")
        else:
            print("1. Failed")
    
    def test_merge1(self):
        print()
        if is_sorted(merge_sort(self.arr)):
            print("1. Sorted")
        else:
            print("1. Failed")
    
    def test_merge2(self):
        print()
        if is_sorted(merge_sort_with_queue(self.arr)):
            print("2. Sorted")
        else:
            print("2. Failed")
    
    def test_quick(self):
        print()
        if is_sorted(quick_sort(self.arr, 0, len(self.arr)-1)):
            print("1. Sorted")
        else:
            print("1. Failed")
    
    def test_quick2(self):
        print()
        print(quick_sort_with_queue(self.arr))
    
    def test_quick3(self):
        print()
        print(quick_sort_with_stack(self.arr))