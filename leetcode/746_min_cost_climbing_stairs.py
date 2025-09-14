# https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        total_cost = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            total_cost[i] = min(total_cost[i - 1] + cost[i - 1], total_cost[i - 2] + cost[i - 2])
        return total_cost[-1]
