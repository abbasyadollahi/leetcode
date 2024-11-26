# https://leetcode.com/problems/4sum/


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        def three_sum(nums: list[int], target: int) -> set[tuple[int, int, int]]:
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
                for combo in two_sum(nums[i + 1 :], target - num)
            }

        return {
            tuple(sorted([num, *combo]))
            for i, num in enumerate(nums[:-3])
            for combo in three_sum(nums[i + 1 :], target - num)
        }
