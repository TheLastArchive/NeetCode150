import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Arrays_and_Hashing.longest_consecutive as aah

class TestContainsDuplicates(unittest.TestCase):
    def test_correct(self):
        solution = aah.Solution()
        self.assertEqual(solution.longestConsecutive([100,4,200,1,3,2]), 4)
        self.assertEqual(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)
        self.assertEqual(solution.longestConsecutive([0,1,3,2,1,4]), 5)
        self.assertEqual(solution.longestConsecutive([1,0,-1]), 3)
        self.assertEqual(solution.longestConsecutive([]), 0)
        self.assertEqual(solution.longestConsecutive([0]), 1)
        

if __name__ == '__main__':
    unittest.main()