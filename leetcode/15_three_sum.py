# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        prev = None
        combinations = []
        length = len(nums) - 1

        for i, c in enumerate(nums):
            if c == prev:
                continue

            prev = c
            l = i + 1
            r = length

            while l < r:
                nl, nr = nums[l], nums[r]

                if nl + nr + c < 0:
                    l += 1
                elif nl + nr + c > 0:
                    r -= 1
                else:
                    combinations.append([c, nl, nr])
                    while nl == nums[l] and l < length:
                        l += 1
                    while nr == nums[r] and r > i:
                        r -= 1
        return combinations

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def two_sum(nums: list[int], target: int) -> set[tuple[int, int]]:
            seen = set()
            doubles = set()
            for num in nums:
                if target - num in seen:
                    doubles.add((num, target - num))
                else:
                    seen.add(num)

            return doubles

        return {
            tuple(sorted([num, *combo]))
            for i, num in enumerate(nums[:-2])
            for combo in two_sum(nums[i+1:], -num)
        }
