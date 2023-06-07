# type : two pointer
# description
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # base profit (if there is no profitable choice)
        maxP = 0
        # current lowest price
        curLow = prices[0]
        for p in prices:
            # if the current price is lower than the current lowest price, update the current lowest price
            if p - curLow < 0:
                curLow = p
            # if the current price is higher than the current lowest price, update the max profit
            else:
                maxP = max(maxP, p-curLow)
        
        return maxP