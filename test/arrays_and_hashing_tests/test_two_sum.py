import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Arrays_and_Hashing.two_sum as aah

class TestTwoSum(unittest.TestCase):
    def test_correct(self):
        solution = aah.Solution()
        self.assertEqual(solution.twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(solution.twoSum([3,2,4], 6), [1,2])
        self.assertEqual(solution.twoSum([3,3], 6), [0,1])
        
        

if __name__ == '__main__':
    unittest.main()