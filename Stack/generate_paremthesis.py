"""
https://leetcode.com/problems/generate-parentheses/
"""

# WIP

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output = []
        left = right = 1

        while left <= n:
            open_count = closed_count = 0
            curr_seq = ""
            while open_count != n or closed_count != n:
                curr_seq += "(" * left
                open_count += 1 * left
                while open_count > n:
                    # 'removes' the last character
                    curr_seq = curr_seq[:-1]
                    open_count -= 1
                curr_seq += ")" * right
                closed_count += 1 * right
                while closed_count > n:
                    curr_seq = curr_seq[:-1]
                    closed_count -= 1
            output.append(curr_seq)
            if left == right:
                left += 1
            else:
                right += 1
        print(output)
        return output
