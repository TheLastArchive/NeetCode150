import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Stack.min_stack as min_stack


class TestMinStack(unittest.TestCase):

    def test_correct_1(self):
        stack = min_stack.MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)
        stack.pop()
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.getMin(), -2)

    def test_correct_2(self):
        stack = min_stack.MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-1)
        self.assertEqual(stack.getMin(), -2)
        self.assertEqual(stack.top(), -1)
        stack.pop()
        self.assertEqual(stack.getMin(), -2)


if __name__ == '__main__':
    unittest.main()