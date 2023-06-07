"""
https://leetcode.com/problems/trapping-rain-water/
"""

class Solution:
    """
    This solution works but can be slow with comedically large arrays
    """
    def trap(self, height: list[int]) -> int:
        
        total = 0
        left = 0
        while left < len(height) - 1:
            left_height = height[left]
            if height[left + 1] >= left_height:
                left += 1
                continue
            
            right = len(height) - 1
            right_wall_index = right
            right_height = 0
            while right != left:
                #reset the volume if a suitable right wall 
                #closer to the left wall has been found
                #and store the index for later
                if height[right] >= left_height or height[right] >= right_height:
                    curr_vol = 0
                    right_wall_index = right
                    right_height = height[right]
                else:
                    curr_vol += min(left_height, right_height) - height[right]
                right -= 1
            
            total += curr_vol
            left = right_wall_index
            
        return total



    
            

                