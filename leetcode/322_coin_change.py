# https://leetcode.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for total in range(amount + 1):
            for coin in coins:
                if coin <= total:
                    dp[total] = min(dp[total], 1 + dp[total-coin])

        return dp[amount] if dp[amount] != float('inf') else -1
