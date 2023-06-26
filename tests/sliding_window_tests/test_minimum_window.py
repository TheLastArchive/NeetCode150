import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Sliding_Window as sw

class TestMinimumWindow(unittest.TestCase):
    def test_correct(self):
        solution = sw.Solution()
        self.assertEqual("BANC", solution.minWindow("ADOBECODEBANC", "ABC"))
        self.assertEqual("a", solution.minWindow("a", "a"))
        self.assertEqual("", solution.minWindow("a", "aa"))

        

if __name__ == '__main__':
    unittest.main()