"""
https://leetcode.com/problems/valid-palindrome/
"""

from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = deque()
        backward = deque()
        
        for char in s:
            if not char.isalnum(): continue
            forward.append(char.lower())
            backward.appendleft(char.lower())
        return forward == backward

