# http://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        r = 0
        flips = 0
        max_length = 0
        while r < len(nums):
            if nums[r] == 1 or flips < k:
                flips += nums[r] == 0 and flips < k
                r += 1
            else:
                max_length = max(max_length, r - l)
                while nums[l] == 1:
                    l += 1
                flips -= 1
                l += 1

        return max(max_length, r - l)
