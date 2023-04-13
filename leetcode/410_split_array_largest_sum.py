# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        maximum = max(nums)
        total = sum(nums)

        def can_split(capacity: int) -> bool:
            load = 0
            loads = 0
            for num in nums:
                load += num
                if load > capacity:
                    load = num
                    loads += 1
                if loads == k:
                    return False

            return True

        l = maximum
        r = total
        while l < r:
            m = (l + r) // 2
            if can_split(m):
                r = m
            else:
                l = m + 1

        return l
