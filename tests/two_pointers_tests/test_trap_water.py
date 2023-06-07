import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Two_Pointers as tp
from random import randint

class TestTrapWater(unittest.TestCase):
    
    """
    Tests correctness
    """
    def test_trap(self):
        solution = tp.Solution()
        self.assertEqual(6, solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        self.assertEqual(9, solution.trap([4,2,0,3,2,5]))
        self.assertEqual(1, solution.trap([4,2,3]))
        self.assertEqual(26, solution.trap([0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]))
        self.assertEqual(3, solution.trap([9,6,8,8,5,6,3]))
    
    """
    Tests several thousand calls, doesn't check correctness
    """
    def test_stress(self):
        solution = tp.Solution()
        for i in range(5):
            test_set = [randint(1, 100000) for i in range(2 * 10000)]
            self.assertTrue(solution.trap(test_set) >= 0)
    
    """
    Checks the worst case scenario, doesn't check correctness
    """
    def test_worst_case(self):
        solution = tp.Solution()
        num = 100000
        test_set = []
        for i in range(10000):
            test_set.append(num)
            test_set.append(0)
            num -= 1
        self.assertTrue(solution.trap(test_set) >= 0)
    

if __name__ == '__main__':
    unittest.main()