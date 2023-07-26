import unittest
# I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Stack.generate_paremthesis as stack


class TestGenerateParenthesis(unittest.TestCase):

    def test_correct(self):
        solution = stack.Solution()
        self.assertCountEqual(["((()))", "(()())", "(())()", "()(())", "()()()"],
                              solution.generateParenthesis(3))
        self.assertCountEqual(["()"],
                              solution.generateParenthesis(1))


if __name__ == '__main__':
    unittest.main()
