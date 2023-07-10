"""
https://leetcode.com/problems/valid-parentheses/
"""
from collections import deque


class Solution:

    def isValid(self, s: str) -> bool:

        stack = deque()
        opens = ["(", "[", "{"]
        text = list(s)
        for i, char in enumerate(text):
            # Check if there is a closed bracket before an open bracket
            if char not in opens and len(stack) == 0:
                return False
            if char in opens:
                # Store the index of the open bracket
                stack.append(i)
                continue

            top = stack.pop()
            if not self.do_brackets_match(left=text[top], right=char):
                return False
        # If the stack is empty then all matches are found
        return len(stack) == 0

    def do_brackets_match(self, left, right) -> bool:
        return (left + right) in ["()", "[]", "{}"]
