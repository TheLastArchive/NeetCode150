import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Two_Pointers.three_sum as tp

class TestThreeSum(unittest.TestCase):
    def test_correct(self):
        solution = tp.Solution()
        self.assertEqual([[-1,-1,2],[-1,0,1]], solution.threeSum([-1,0,1,2,-1,-4]))
        self.assertEqual([], solution.threeSum([0, 1, 1]))
        self.assertEqual([[0, 0, 0]], solution.threeSum([0, 0, 0]))
        self.assertEqual([[0, 0, 0]], solution.threeSum([0, 0, 0, 0]))
        

if __name__ == '__main__':
    unittest.main()