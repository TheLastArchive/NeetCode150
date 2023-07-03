"""
https://leetcode.com/problems/two-sum/
"""

class Solution:
    # Double nested for-loop = yucky. Dynamic would be much better
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     for i, x in enumerate(nums):
    #         for j, y in enumerate(nums[i+1:], start=i+1):
    #             if x + y == target: return [i, j]
    
    #This solution is much smarter than my dynamic implementation
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {} #Used to map the visited values {value: index}
        for index, value in enumerate(nums):
            #Check if we've found the difference
            if (target - value) in visited:
                return [visited[target - value], index]
            visited[value] = index