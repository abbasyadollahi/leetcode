# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)

        max_count = 0
        for num in nums:
            if num - 1 not in nums:
                count = 0
                while num in nums:
                    num += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count

    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        count = 1
        max_count = 0
        nums.sort()
        for i, num in enumerate(nums):
            diff = num - nums[i-1]
            if diff == 1:
                count += 1
            elif diff == 0:
                continue
            else:
                max_count = max(max_count, count)
                count = 1

        return max(max_count, count)
