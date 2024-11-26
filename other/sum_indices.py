class Solution:
    def sumIndices(self, num_list: list[int], target: int) -> list[int]:
        for i, value in enumerate(num_list):
            for j in range(i + 1, len(num_list)):
                if (value + num_list[j]) == target:
                    return [i, j]
        return [0, 0]

    def sumIndices(self, num_list: list[int], target: int) -> list[int]:
        num_set = set(num_list)
        for i, value in enumerate(num_list):
            if (target - value) in num_set:
                return [i, num_list.index(target - value)]
        return [0, 0]


sol = Solution()
assert sol.sumIndices([1, 2, 3, 4, 5, 6], 5) == [0, 3]
