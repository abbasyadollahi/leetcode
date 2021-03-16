# https://leetcode.com/problems/maximum-erasure-value/

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        tail = 0
        current = 0
        largest = 0
        seen = set()

        for num in nums:
            if num in seen:
                largest = max(largest, current)
                while nums[tail] != num:
                    seen.remove(nums[tail])
                    current -= nums[tail]
                    tail += 1
                tail += 1
            else:
                seen.add(num)
                current += num
        return max(largest, current)
