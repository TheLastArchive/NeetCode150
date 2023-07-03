import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Arrays_and_Hashing.product_array_except_self as aah

class TestContainsDuplicates(unittest.TestCase):
    def test_correct(self):
        solution = aah.Solution()
        self.assertEqual(solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(solution.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])


if __name__ == '__main__':
    unittest.main()