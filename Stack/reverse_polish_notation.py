"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
from collections import deque


class Solution:

    def do_operation(self, x, y, operator):
        if operator == "+":
            return x + y
        if operator == "-":
            return x - y
        if operator == "*":
            return x * y
        if operator == "/":
            # certain division won't round towards 0  ie -1/2 == -1
            # Floating point to int will make it 0
            return int(x / y)

    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()
        operators = ["+", "-", "/", "*"]
        for token in tokens:
            if token not in operators:
                stack.append(token)
                continue
            y = int(stack.pop())
            x = int(stack.pop())
            total = self.do_operation(x, y, token)
            stack.append(total)

        return int(stack[0])
