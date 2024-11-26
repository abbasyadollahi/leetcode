# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)

        length = 10
        max_int = 214748364

        num = 0
        digits = 0
        while x > 0:
            digits += 1
            if digits == length:
                rem = x % 10
                if num > max_int:
                    return 0
                if negative and num == max_int and rem > 8:
                    return 0
                if not negative and num == max_int and rem > 7:
                    return 0
            num *= 10
            num += x % 10
            x //= 10
        return -num if negative else num
