# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        bags = 0
        for rock in sorted(total - current for total, current in zip(capacity, rocks)):
            if additionalRocks < rock:
                return bags
            else:
                additionalRocks -= rock
                bags += 1
        return bags
