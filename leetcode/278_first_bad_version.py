# https://leetcode.com/problems/first-bad-version/


def isBadVersion(version: int) -> bool:
    """The isBadVersion API is already defined for you."""
    ...


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l
