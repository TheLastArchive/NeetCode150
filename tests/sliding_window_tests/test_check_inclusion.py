import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Sliding_Window as sw

class TestCheckInclusion(unittest.TestCase):
    def test_correct(self):
        solution = sw.Solution()
        self.assertTrue(solution.checkInclusion("ab", "eidbaooo"))
        self.assertFalse(solution.checkInclusion("ab", "eidboaoo"))
        self.assertTrue(solution.checkInclusion("aab", "eidabaoao"))
        self.assertFalse(solution.checkInclusion("aab", "eidaaobao"))
        self.assertTrue(solution.checkInclusion("aab", "eidaaabaobao"))
        self.assertFalse(solution.checkInclusion("aab", "aa"))
        self.assertFalse(solution.checkInclusion("hello", "ooolleoooleh"))
        self.assertTrue(solution.checkInclusion("adc", "dcda"))

        

if __name__ == '__main__':
    unittest.main()