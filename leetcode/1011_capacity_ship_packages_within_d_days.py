# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        max_weight = max(weights)
        total_weight = sum(weights)

        def can_ship(capacity: int) -> bool:
            load = 0
            loads = 0
            for weight in weights:
                load += weight
                if load > capacity:
                    load = weight
                    loads += 1
                if loads == days:
                    return False

            return True

        l = max_weight
        r = total_weight
        while l < r:
            m = (l + r) // 2
            if can_ship(m):
                r = m
            else:
                l = m + 1

        return l
