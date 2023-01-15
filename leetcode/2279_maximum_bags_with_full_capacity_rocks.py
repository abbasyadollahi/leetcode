# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        bags = 0
        for rock in sorted(total - current for total, current in zip(capacity, rocks)):
            if additionalRocks < rock:
                return bags
            else:
                additionalRocks -= rock
                bags += 1
        return bags
