import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Sliding_Window.max_profit as sw

class TestMaxProfit(unittest.TestCase):
    def test_correct(self):
        solution = sw.Solution()
        self.assertEqual(5, solution.maxProfit([7,1,5,3,6,4]))
        self.assertEqual(5, solution.maxProfit([7,3,5,1,6,4]))
        self.assertEqual(7, solution.maxProfit([5,12,3,4]))
        self.assertEqual(9, solution.maxProfit([3,10,4,12]))
        self.assertEqual(0, solution.maxProfit([7,6,4,3,1]))


if __name__ == '__main__':
    unittest.main()