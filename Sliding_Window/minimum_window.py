"""
INCOMPLETE
This is hard :(
https://leetcode.com/problems/minimum-window-substring/
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        t_list = list(t)
        while True:
            while s[left] not in t:
                left += 1
            
        return

