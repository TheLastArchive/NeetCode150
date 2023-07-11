import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Stack.reverse_polish_notation as stack


class TestReversePolishNotation(unittest.TestCase):

    def test_correct(self):
        solution = stack.Solution()
        self.assertEqual(solution.evalRPN(["2","1","+","3","*"]), 9)
        self.assertEqual(solution.evalRPN(["4","13","5","/","+"]), 6)
        self.assertEqual(solution.evalRPN(["18"]), 18)
        self.assertEqual(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)


if __name__ == '__main__':
    unittest.main()
