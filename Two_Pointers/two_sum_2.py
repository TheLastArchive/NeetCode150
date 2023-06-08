"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from collections import defaultdict

class Solution:
    """
    Makes use of two pointers since the array is sorted, this is pretty effecient
    """
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left != right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                # return index + 1 since solution wants index to be 1-based
              return [left + 1,  right + 1]
            if numbers[right] > target or curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1
    
    """
    Uses the same method as the previous two sum solution and still works really well.
    I'd still use this method over the other solution as it works whether the array is 
    sorted or not.
    """
    def twoSumMap(self, numbers: list[int], target: int) -> list[int]:
        visited = defaultdict()
        for index, value in enumerate(numbers):
            if target - value in visited:
                return [visited[target-value], index + 1]
            visited[value] = index + 1
            
            




