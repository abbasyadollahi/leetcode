# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
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

    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
