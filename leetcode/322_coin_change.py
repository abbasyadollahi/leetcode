# https://leetcode.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for a in range(amount + 1):
                if coin <= a:
                    dp[a] = min(dp[a], 1 + dp[a-coin])

        return dp[amount] if dp[amount] < float('inf') else -1
