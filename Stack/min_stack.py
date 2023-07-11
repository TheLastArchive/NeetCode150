"""
https://leetcode.com/problems/min-stack/
"""

class MinStack:

    def __init__(self):
        # Linked list will likely be faster
        self.stack = []
        self.curr_min = None

    def push(self, val: int) -> None:
        if self.curr_min is None or val < self.curr_min:
            self.curr_min = val
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        # Check if a new min must be found
        popped = self.stack.pop(-1)
        if popped == self.curr_min and self.stack:
            self.curr_min = min(self.stack)
        elif popped == self.curr_min and not self.stack:
            self.curr_min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min

