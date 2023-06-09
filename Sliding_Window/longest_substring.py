"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Can be made quicker with a set
        substr = deque()
        max_substr = 0
        for letter in s:
            while letter in substr:
                substr.popleft()
            substr.append(letter)
            max_substr = max(len(substr), max_substr)

        return max_substr


    def lengthOfLongestSubstringSet(self, s: str) -> int:
        
        substr = set()
        max_substr = 0
        i = 0
        for letter in s:
            while letter in substr:
                #Sets are unordered so we'll need to iterate through the origingal list
                substr.remove(s[i])
                i += 1
            substr.add(letter)
            max_substr = max(len(substr), max_substr)

        return max_substr
    
