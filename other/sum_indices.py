from typing import List


class Solution:
    def sumIndices(self, num_list: List[int], target: int) -> List[int]:
        for idx, value in enumerate(num_list):
            for j in range(idx + 1, len(num_list)):
                if (value + num_list[j]) == target:
                    return [idx, j]
        return [0, 0]

    def sumIndices(self, num_list: List[int], target: int) -> List[int]:
        num_set = set(num_list)
        for idx, value in enumerate(num_list):
            if (target - value) in num_set:
                return [idx, num_list.index(target-value)]
        return [0, 0]


sol = Solution()
print(sol.sumIndices([1,2,3,4,5,6], 5))
