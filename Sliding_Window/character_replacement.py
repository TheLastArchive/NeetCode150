"""
https://leetcode.com/problems/longest-repeating-character-replacement/
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2: return len(s)
        char_counts = defaultdict(int)
        max_substr = 0
        left, right = 0, 0
        while right < len(s):
            char_counts[s[right]] += 1
            while (right - left + 1) - max(char_counts.values()) > k:
                char_counts[s[left]] -= 1
                left += 1
            max_substr = max(max_substr, right - left + 1)
            right += 1

            
        return max_substr