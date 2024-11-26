# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        buy = [0] * len(prices)
        sell = [0] * len(prices)
        rest = [0] * len(prices)

        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            rest[i] = max(rest[i - 1], sell[i - 1])

        return sell[-1]
