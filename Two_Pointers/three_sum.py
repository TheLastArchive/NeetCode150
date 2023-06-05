"""
https://leetcode.com/problems/3sum/
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #Sorting not ideal but I can't think of anything else.
        #This is how I would do it in the real world anyway
        nums.sort()
        output = []
        prev_num = None

        for index, num in enumerate(nums):
            #Since the array is sorted, anything past 0 will not sum to 0
            if num > 0: break
            #Skip duplicates
            if prev_num == num: continue
            #From here on, it's basically just two sum 2 with extra checks
            left = index + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else: #curr_sum == 0
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    #Skip duplicates
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
            prev_num = num        
            
        return output
    
    
solution = Solution()
print(f"[[-1, -1, 2],[-1, 0, 1]]: {solution.threeSum([-1, 0, 1, 2, -1, -4])}")
print(f"[]: {solution.threeSum([0, 1, 1])}")
print(f"[0, 0, 0]: {solution.threeSum([0, 0, 0])}")
print(f"[[0, 0, 0]]: {solution.threeSum([0, 0, 0, 0])}")