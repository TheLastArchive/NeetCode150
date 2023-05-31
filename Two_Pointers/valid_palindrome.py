from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = deque()
        backward = deque()
        
        for char in s:
            if not char.isalnum(): continue
            forward.append(char.lower())
            backward.appendleft(char.lower())
        return forward == backward
    
    def test(self, s: str):
        print(s.isalnum())
        return

solution = Solution()
print(f'True: {solution.isPalindrome("A man, a plan, a canal: Panama")}')
print(f'False: {solution.isPalindrome("race a car")}')
print(f'True: {solution.isPalindrome(" ")}')
print(f'False: {solution.isPalindrome("0P")}')
