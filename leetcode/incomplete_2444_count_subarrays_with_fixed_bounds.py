# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/


class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        def shrink(
            l: int,
            r: int,
            min_count: int,
            max_count: int,
            visited: set[tuple[int, int]],
        ) -> int:
            if not min_count or not max_count or (l, r) in visited:
                return 0

            visited.add((l, r))
            start = shrink(
                l + 1,
                r,
                min_count - (nums[l] == minK),
                max_count - (nums[l] == maxK),
                visited,
            )
            end = shrink(
                l,
                r - 1,
                min_count - (nums[r] == minK),
                max_count - (nums[r] == maxK),
                visited,
            )
            return 1 + start + end

        l = 0
        bounds = range(minK, maxK + 1)
        total = 0
        while l < len(nums):
            r = l
            min_k_count = 0
            max_k_count = 0
            while r < len(nums) and nums[r] in bounds:
                min_k_count += nums[r] == minK
                max_k_count += nums[r] == maxK
                r += 1
            if min_k_count and max_k_count:
                total += shrink(l, r - 1, min_k_count, max_k_count, set())

            l += r + 1

        return total
