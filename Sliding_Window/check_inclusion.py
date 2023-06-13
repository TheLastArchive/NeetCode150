"""
https://leetcode.com/problems/permutation-in-string/
"""

class Solution:    
    """
    This solution works but can be slow with comedically large strings
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = list(s1)
        for i in range(len(s2)):
            #Check the chars after this point
            while i < len(s2) and s2[i] in chars:
                chars.pop(chars.index(s2[i]))
                #Index will reset on the next run of the for loop
                i += 1
                if not chars:
                    return True
            #resets the list, probably a better way to do this
            chars = list(s1)

        return False