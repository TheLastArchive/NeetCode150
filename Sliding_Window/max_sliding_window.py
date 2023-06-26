"""
https://leetcode.com/problems/sliding-window-maximum/
"""

from collections import deque

class Solution:
    """Simple solution, but slow with comedically large arrays"""
    def maxSlidingWindowSimple(self, nums: list[int], k: int) -> list[int]:
        left, right = 0, k
        maximums = []
        while right <= len(nums):
            maximums.append(max(nums[left:right]))
            left += 1
            right += 1
        return maximums
    
    
    """Slightly faster but still not good enough for comedically large arrays"""
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        #Use deques for quick pops and appends
        window = deque(nums[:k])
        queue = deque(nums[k:])
        maximums = []
        curr_max = max(window)
        while True:    
            maximums.append(curr_max)
            #If the queue is empty, all checks have been completed
            if len(queue) == 0: 
                return maximums

            new_val = queue.popleft()
            window.append(new_val)
            
            if new_val > curr_max: 
                curr_max = new_val
            if window.popleft() == curr_max:
                curr_max = max(window)