import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Stack.valid_parentheses as stack

class TestValidParentheses(unittest.TestCase):
    
    def test_correct(self):
        solution = stack.Solution()
        self.assertTrue(solution.isValid("()"))
        self.assertTrue(solution.isValid("()[]{}"))
        self.assertFalse(solution.isValid("(]"))


if __name__ == '__main__':
    unittest.main()