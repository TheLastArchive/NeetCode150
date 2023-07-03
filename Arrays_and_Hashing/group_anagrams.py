"""
https://leetcode.com/problems/group-anagrams/
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        sorted_strs_dict = defaultdict(list)
        for index, word in enumerate(strs):
            #Sort word to make it easier to compare
            sorted_word = ''.join(sorted(word))
            sorted_strs_dict[sorted_word].append(strs[index])
        return [*sorted_strs_dict.values()]