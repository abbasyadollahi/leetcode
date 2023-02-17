# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev = set()
        for i, n in enumerate(nums):
            if target - n in prev:
                return [nums.index(target - n), i]
            else:
                prev.add(n)

        return None


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 23))
print(sol.twoSum([2, 7, 11, 15], 22))
