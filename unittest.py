import unittest   # The test framework

from  bubble_sort import* # same directory as test files
from bucket_sort import *
from counting_sort import *
from heap_sort import *
from insertion_sort import *
from merge_sort import *
from quick_select import *
from quick_sort import *
from radix_sort import *
from selection_sort import*
import random

class Test_SortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.sortedList = [1,2,3,4,5]
        self.unsortedList = [5,4,3,2,1]
        self.oneItem=[1]
        self.noItems=[]

    def test_bubble_sort(self):
        print(f'Bubble Sort is being tested with this list: {self.unsortedList}')
        self.assertListEqual(self.sortedList,bubble_sort(self.unsortedList))
        print(f'Bubble Sort Passed: {bubble_sort(self.unsortedList)}')

    def test_bucket_sort(self):
        print(f'Bucket sort is being tested on the following list: {self.unsortedList}')
        self.assertListEqual(self.sortedList,bucket_sort(self.unsortedList))
        print(f'Bucket Sort Passed ',bucket_sort(self.unsortedList))

    def test_counting_sort(self):
        print(f'Counting sort is being tested on the  following list: {self.unsortedList}')
        self.assertListEqual(self.sortedList,counting_sort(self.unsortedList))
        print(f'Counting Sort Passed', counting_sort(self.unsortedList))

    def test_heap_sort(self):
        print(f'Heap Sort is being  tested on the following list: {self.unsortedList}')
        self.assertListEqual(self.sortedList,heap_sort(self.unsortedList))
        print(f'Heap Sort Passed: {heap_sort(self.unsortedList)}')

    def test_insertion_sort(self):
        print(f'Insertion Sort is being tested on the following list: {self.unsortedList}')
        self.assertListEqual(self.sortedList,insertion_sort(self.unsortedList))
        print(f'Insertion Sort Passed: {insertion_sort(self.unsortedList)}')

    def test_merge_sort(self):
        print(f'Merge Sort is being tested on the following list: {self.unsortedList}')
        self.assertListEqual(self.sortedList,merge_sort(self.unsortedList))
        print(f'Merge Sort Passed: {merge_sort(self.unsortedList)}')

    def test_quick_select(self):
        pass
        #print(f'Quick Sort is being  tested on the following list: {self.unsortedList}')
        #self.assertListEqual(self.sortedList,quick_select(self.unsortedList))
    
    

    def test_quick_sort(self):
        print(f'\n quick sort  is being tested on the following list: {self.unsortedList} \n')
        self.assertListEqual(self.sortedList,quick_sort(self.unsortedList))
        print(f'Quick Sort Passed{quick_sort(self.unsortedList)}')

    def test_radix_sort(self):
        print(f'Radix Sort is being tested on the following list: {self.unsortedList}')
        self.assertListEqual(self.sortedList,radix_sort(self.unsortedList))
        print(f'Radix Sort Passed: {self.unsortedList}')

    def test_selection_sort(self):
        print(f'Selection Sort is being tested on the following list: {self.unsortedList}')
        self.assertListEqual(self.sortedList,selection_sort(self.unsortedList))
        print(f'Selection Sort Passed: {selection_sort(self.unsortedList)}')
    
    def test_edge_cases(self):
        print("Edge Cases: \n")
        
        print(f'Empty List: {self.noItems}')
        self.assertListEqual(self.noItems,bubble_sort(self.noItems))
        print(f'Empty List test passed: {bubble_sort(self.noItems)}')
        
        print(f'One Item: {self.oneItem}')
        self.assertListEqual(self.oneItem,bubble_sort(self.oneItem))
        print(f'One Item Test Passed: {bubble_sort(self.oneItem)}')

        print(f'Already sorted {self.sortedList}')
        self.assertListEqual(self.sortedList,radix_sort(self.sortedList))
        print(f'Already sorted test Passed {radix_sort(self.sortedList)}')


if _name_ == '_main_':
    unittest.main()
