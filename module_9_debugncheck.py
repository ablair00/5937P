import unittest
import itertools as it

def addnumberstocount(n):
    for n in it.count():
        if 1000 < n < 1010:
            print(n);
        if n > 10000:
            break
        
class TestAddNumbersToCount(unittest.TestCase):
    def test_add_numbers_to_count_success(self):
        actual = addnumberstocount(number_list=[range(0,20000)])
        expected = {"1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009"}
        self.assertEqual(actual, expected)
        
