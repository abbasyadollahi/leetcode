# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        unique_jewels = set(jewels)
        return sum(1 for stone in stones if stone in unique_jewels)
