"""
https://leetcode.com/problems/top-k-frequent-elements/
"""

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = defaultdict(int) #{number: frequency}
        for i in nums:
            freq[i] += 1
        #Sort the dict by value    
        sort_freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
        return [x[0] for x in sort_freq[:k]]