class Solution:
    """
    This solution is fine and pretty fast. It checks each element in both directions
    NeetCode's solution finds a value that doesn't have a 'left' value (ie the first value in a sequence) 
    and just checks greater values from there
    """
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if len(nums) == 0: return 0
        #Convert to sets to remove duplicates and make use of O(1) lookup
        nums = set(nums)
        longest_seq = 0
        while len(nums) > 0:
            curr_seq = 1
            num = left = right = nums.pop()
            #check left
            while True:
                if left-1 not in nums: break
                curr_seq += 1
                left -= 1 
                nums.discard(left)
            #check right
            while True:
                if right+1 not in nums: break
                curr_seq += 1
                right += 1
                nums.discard(right)
            
            if curr_seq > longest_seq: 
                longest_seq = curr_seq
                
        return longest_seq
    
    """
    NeetCode's solution, a lot more compact
    """
    def longestConsecutiveNeet(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        
        nums = set(nums)
        longest_seq = 0
        for val in nums:
            curr_seq = 1
            #We're trying to find that 'smallest' value of a sequence
            if val-1 in nums: continue
            while (val + curr_seq) in nums:
                curr_seq += 1

            if curr_seq > longest_seq: 
                longest_seq = curr_seq
                
        return longest_seq
            
            
if __name__ == '__main__':
    solution = Solution()
    print(f"4: {solution.longestConsecutive([100,4,200,1,3,2])}")
    print(f"9: {solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])}")
    print(f"5: {solution.longestConsecutive([0,1,3,2,1,4])}")
    print(f"3: {solution.longestConsecutive([1,0,-1])}")
    print(f"0: {solution.longestConsecutive([])}")
    print(f"1: {solution.longestConsecutive([0])}")
    