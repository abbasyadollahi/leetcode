# https://leetcode.com/problems/k-radius-subarray-averages/


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        averages = []
        diameter = 2 * k + 1
        for i in range(len(nums)):
            if i - k < 0 or i + k > len(nums) - 1:
                averages.append(-1)
            else:
                average = (prefix_sum[i + k + 1] - prefix_sum[i - k]) / diameter
                averages.append(int(average))

        return averages
