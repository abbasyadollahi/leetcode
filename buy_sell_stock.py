# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices or len(prices) == 1:
            return 0

        profit = 0
        min_price = prices[0]
        for p in prices:
            if p - min_price > profit:
                profit = p - min_price
            elif p < min_price:
                min_price = p

        return profit
