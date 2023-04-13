# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums

        list1 = self.sortArray(nums[:len(nums)//2])
        list2 = self.sortArray(nums[len(nums)//2:])

        return self.merge(list1, list2)

    def merge(self, list1: list[int], list2: list[int]) -> list[int]:
        sorted_list = []
        i1 = 0
        i2 = 0

        while i1 < len(list1) and i2 < len(list2):
            if list1[i1] < list2[i2]:
                sorted_list.append(list1[i1])
                i1 += 1
            else:
                sorted_list.append(list2[i2])
                i2 += 1

        while i1 < len(list1):
            sorted_list.append(list1[i1])
            i1 += 1

        while i2 < len(list2):
            sorted_list.append(list2[i2])
            i2 += 1

        return sorted_list
