# https://leetcode.com/problems/next-closest-time/

from itertools import product


class Solution:
    def latestTime(self, time: str) -> str:
        digits = set(time.replace(':', ''))
        hh, mm = time[:2], time[3:]

        if len(digits) == 1:
            return time

        permutations = [''.join(num) for num in product(digits, repeat=2)]

        mmm = max([num for num in permutations if num < mm]) if mm != '00' else max([num for num in permutations if num < '60'])
        hhh = hh
        if mmm >= mm:
            hhh = max([num for num in permutations if num < hh]) if hh != '00' else max([num for num in permutations if num < '24'])

        return hhh + ':' + mmm

sol = Solution()
print(sol.latestTime('11:01'))
print(sol.latestTime('10:00'))
print(sol.latestTime('22:22'))
print(sol.latestTime('22:21'))
print(sol.latestTime('00:01'))
print(sol.latestTime('23:59'))
