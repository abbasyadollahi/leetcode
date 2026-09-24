# https://leetcode.com/problems/maximum-average-subarray-i/


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        average = max_average = sum(nums[:k])
        l = 1
        r = k
        while r < len(nums):
            average = average - nums[l - 1] + nums[r]
            max_average = max(average, max_average)
            l += 1
            r += 1
        return max_average / k
