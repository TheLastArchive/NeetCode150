import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Sliding_Window.max_sliding_window as sw

class TestMaxSlidingWindow(unittest.TestCase):
    def test_correct(self):
        solution = sw.Solution()
        self.assertEqual([3,3,5,5,6,7], solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
        self.assertEqual([1], solution.maxSlidingWindow([1], 1))

        

if __name__ == '__main__':
    unittest.main()