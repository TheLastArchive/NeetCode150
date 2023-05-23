import numpy

class Solution:
    """
    Works alright but not very effecient when the array is comically large.
    """
    # def productExceptSelf(self, nums: list[int]) -> list[int]:
    #     output = [0] * len(nums)
    #     for index, value in enumerate(nums):
    #         nums[index] = 1
    #         output[index] = numpy.prod(nums)
    #         nums[index] = value
        
    #     return output

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)
        prev = 1
        post = 1
        for i, x in enumerate(nums):
            output[i] = prev
            prev *= x
        #Work through the lists backwards now
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]
            
        return output