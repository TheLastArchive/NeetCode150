import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Two_Pointers.valid_palindrome as tp

class TestValidPalindrome(unittest.TestCase):
    def test_correct_two_pointer(self):
        solution = tp.Solution()
        self.assertTrue(solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(solution.isPalindrome("race a car"))
        self.assertTrue(solution.isPalindrome(" "))
        self.assertFalse(solution.isPalindrome("0P"))

        

if __name__ == '__main__':
    unittest.main()