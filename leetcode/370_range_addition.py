# https://leetcode.com/problems/range-addition


class Solution:
    def getModifiedArray(self, length: int, updates: list[int]) -> int:
        array = [0] * length

        for left, right, amount in updates:
            array[left - 1] += amount
            if right < length:
                array[right] -= amount

        for i in range(1, length):
            array[i] += array[i - 1]

        return max(array)
