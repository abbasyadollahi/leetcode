# https://leetcode.com/problems/moving-average-from-data-stream/


class Solution:
    def __init__(self, size: int) -> None:
        self.size = size
        self.nums = []

    def next(self, val: int) -> float:
        self.nums.append(val)
        if len(self.nums) > self.size:
            self.nums.pop(0)

        return sum(self.nums) / len(self.nums)


sol = Solution(3)
print(sol.next(1))
print(sol.next(10))
print(sol.next(3))
print(sol.next(5))
