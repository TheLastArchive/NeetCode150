import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Sliding_Window as sw

class TestCharacterReplacement(unittest.TestCase):
    def test_correct(self):
        solution = sw.Solution()
        self.assertEqual(4, solution.characterReplacement("ABAB", 2))
        self.assertEqual(4, solution.characterReplacement("AABABBA", 1))
        self.assertEqual(5, solution.characterReplacement("ABBBABA", 1))
        self.assertEqual(5, solution.characterReplacement("AAAAB", 1))
        self.assertEqual(5, solution.characterReplacement("AAAABBBB", 1))
        self.assertEqual(1, solution.characterReplacement("A", 1))
        self.assertEqual(0, solution.characterReplacement("", 1))

if __name__ == '__main__':
    unittest.main()