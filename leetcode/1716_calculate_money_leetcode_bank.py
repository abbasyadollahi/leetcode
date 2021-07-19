# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

import math


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n / 7
        return (
            sum(i * 7 + 28 for i in range(math.floor(weeks))) +
            sum(range(math.ceil(weeks), math.ceil(weeks) + n % 7))
        )
