"""
https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_volume = 0
        while left < right:
            curr_volume = 0
            if height[left] <= height[right]:
                curr_volume = height[left] * (right - left)
            else:
                curr_volume = height[right] * (right - left)
            
            if curr_volume > max_volume:
                max_volume = curr_volume
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return max_volume