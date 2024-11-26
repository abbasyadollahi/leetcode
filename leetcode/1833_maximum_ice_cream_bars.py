# https://leetcode.com/problems/maximum-ice-cream-bars/


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        dp = [[0] * (coins + 1) for _ in range(len(costs) + 1)]

        for i, cost in enumerate(costs, 1):
            for j in range(1, coins + 1):
                if j - cost < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + 1)

        return dp[len(costs)][coins]

    def maxIceCream(self, costs: list[int], coins: int) -> int:
        ice_creams = 0
        for cost in sorted(costs):
            if coins < cost:
                return ice_creams
            else:
                coins -= cost
                ice_creams += 1
        return ice_creams
