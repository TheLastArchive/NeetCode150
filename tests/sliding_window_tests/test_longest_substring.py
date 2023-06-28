import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Sliding_Window.longest_substring as sw

class TestLongestSubstring(unittest.TestCase):
    def test_correct_deque(self):
        solution = sw.Solution()
        self.assertEqual(3, solution.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, solution.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, solution.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(3, solution.lengthOfLongestSubstring("dvdf"))
        self.assertEqual(7, solution.lengthOfLongestSubstring("abcdeafg"))
        self.assertEqual(0, solution.lengthOfLongestSubstring(""))
        self.assertEqual(1, solution.lengthOfLongestSubstring("a"))
        
    def test_correct_set(self):
        solution = sw.Solution()
        self.assertEqual(3, solution.lengthOfLongestSubstringSet("abcabcbb"))
        self.assertEqual(1, solution.lengthOfLongestSubstringSet("bbbbb"))
        self.assertEqual(3, solution.lengthOfLongestSubstringSet("pwwkew"))
        self.assertEqual(3, solution.lengthOfLongestSubstringSet("dvdf"))
        self.assertEqual(7, solution.lengthOfLongestSubstringSet("abcdeafg"))
        self.assertEqual(0, solution.lengthOfLongestSubstringSet(""))
        self.assertEqual(1, solution.lengthOfLongestSubstringSet("a"))

if __name__ == '__main__':
    unittest.main()