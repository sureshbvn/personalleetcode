# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
#  to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

from typing import Optional
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = 0

        # This is because we cant buy and sell the same day.
        high = 1
        maxProfit = 0

        # Iterate till end of array.
        while high < len(prices):

            # If the buying price is less than selling price, we can just start the new
            # search from high.
            if prices[low] > prices[high]:
                low = high
                high = high + 1
            else:
                profit = prices[high] - prices[low]
                maxProfit = max(maxProfit, profit)
                high = high + 1

        return maxProfit

obj = Solution()
assert  obj.maxProfit([7,1,5,3,6,4]) == 5
assert  obj.maxProfit([7,6,4,3,1]) == 0