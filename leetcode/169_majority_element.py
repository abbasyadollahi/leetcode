# https://leetcode.com/problems/majority-element/

from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        element = None

        for num in nums:
            if count == 0:
                element = num
            count += 1 if num == element else -1

        return element
