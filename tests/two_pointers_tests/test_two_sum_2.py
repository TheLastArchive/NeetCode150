import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Two_Pointers as tp

class TestTwoSumTwo(unittest.TestCase):
    def test_correct_two_pointer(self):
        solution = tp.Solution()
        self.assertEqual([1,2], solution.twoSum([2,7,11,15], 9))
        self.assertEqual([1,3], solution.twoSum([2,3,4], 6))
        self.assertEqual([1,2], solution.twoSum([-1,0], -1))
        self.assertEqual([1,3], solution.twoSum([1,2,3,4], 4))
        self.assertEqual([2,3], solution.twoSum([2,3,4], 7))
        self.assertEqual([1,2], solution.twoSum([1,2], 3))
        self.assertEqual([3,4], solution.twoSum([-1000,-1,0,1], 1))
        
        
    def test_correct_map(self):
        solution = tp.Solution()
        self.assertEqual([1,2], solution.twoSumMap([2,7,11,15], 9))
        self.assertEqual([1,3], solution.twoSumMap([2,3,4], 6))
        self.assertEqual([1,2], solution.twoSumMap([-1,0], -1))
        self.assertEqual([1,3], solution.twoSumMap([1,2,3,4], 4))
        self.assertEqual([2,3], solution.twoSumMap([2,3,4], 7))
        self.assertEqual([1,2], solution.twoSumMap([1,2], 3))
        self.assertEqual([3,4], solution.twoSumMap([-1000,-1,0,1], 1))
        

if __name__ == '__main__':
    unittest.main()