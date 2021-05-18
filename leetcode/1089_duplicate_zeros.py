# https://leetcode.com/problems/duplicate-zeros/

from queue import Queue
from typing import List


class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        i = 0
        l = len(nums)
        q = Queue(maxsize=l)

        while i < l:
            if not q.empty():
                q.put(nums[i])
                nums[i] = q.get()

            if nums[i] == 0 and i < l - 1:
                i += 1
                q.put(nums[i])
                nums[i] = 0
            i += 1

    def duplicateZeros(self, nums: List[int]) -> None:
        i = 0
        l = len(nums)
        copy = []

        while i < l:
            num = nums[i]
            copy.append(num)
            i += 1
            if num == 0:
                copy.append(0)

        nums[:l] = copy[:l]

    def duplicateZeros(self, nums: List[int]) -> None:
        count = 0
        l = len(nums)
        lacking = False

        for i, num in enumerate(nums):
            count += 1
            if count == l:
                if num == 0:
                    lacking = True
                break
            if num == 0:
                count += 1
            if count == l:
                break

        j = l - 1
        while i >= 0:
            if nums[i] == 0:
                if lacking:
                    lacking = False
                else:
                    nums[j] = 0
                    j -= 1
            nums[j] = nums[i]
            i -= 1
            j -= 1
