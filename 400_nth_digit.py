# https://leetcode.com/problems/nth-digit/

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n

        total = 9
        digits = 1
        while n > total:
            digits += 1
            total += (9 * digits) * 10 ** (digits - 1)

        power = 10 ** (digits - 1)
        diff = n - (total - (9 * digits) * power) - 1

        return int(str(power + diff//digits)[diff%digits])

sol = Solution()
print(sol.findNthDigit(201))
