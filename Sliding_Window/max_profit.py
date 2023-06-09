"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_price = 0
        max_profit = 0
        
        for price in prices:
            if price > max_price:
                max_price = price
            if max_price - min_price > max_profit:
                max_profit = max_price - min_price
            #If a lower min is found, reset the max
            if price < min_price:
                min_price = price
                max_price = 0
            
        
        #if the number is negative, return 0 
        return max(0, (max_profit))