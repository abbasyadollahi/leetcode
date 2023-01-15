# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [nums1 - nums2, nums2 - nums1]
