import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Two_Pointers.most_water as tp

class TestMostWater(unittest.TestCase):
    
    def test_maxArea(self):
        solution = tp.Solution()
        self.assertEqual(49, solution.maxArea([1,8,6,2,5,4,8,3,7]))
        self.assertEqual(1, solution.maxArea([1,1]))


if __name__ == '__main__':
    unittest.main()