# https://leetcode.com/problems/missing-ranges/

from typing import List


class Solution:
    def strRange(self, start: int, end: int) -> str:
        return f'{start + 1}->{end - 1}' if end - start != 2 else str(start + 1)

    def missingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if lower == upper:
            return []
        if not nums:
            return [self.strRange(lower - 1, upper + 1)]

        ranges = []
        prev = lower

        if prev < nums[0]:
            ranges.append(self.strRange(prev - 1, nums[0]))
            prev = nums[0]

        for num in nums[1:]:
            if num > prev + 1:
                ranges.append(self.strRange(prev, num))
            prev = num

        if prev < upper:
            ranges.append(self.strRange(prev, upper + 1))

        return ranges


sol = Solution()
print(sol.missingRanges([0, 1, 3, 50, 75], 0, 99))
