import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Arrays_and_Hashing.contains_duplicates as aah

class TestContainsDuplicates(unittest.TestCase):
    def test_correct(self):
        solution = aah.Solution()
        self.assertTrue(solution.containsDuplicate([1,2,3,1]))
        self.assertTrue(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
        self.assertFalse(solution.containsDuplicate([1,2,3,4]))
        

if __name__ == '__main__':
    unittest.main()