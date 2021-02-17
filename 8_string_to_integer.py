# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()
        polarity = 1

        if not string:
            return 0
        if string[0] in ('+', '-'):
            polarity = -1 if string[0] == '-' else 1
            string = string[1:]
        if not string or not string[0].isdigit():
            return 0

        digits = []
        for i in range(len(string)):
            if string[i].isdigit():
                digits.append(string[i])
            else:
                break

        max_int = 2 ** 31 - 1
        min_int = -1 * max_int - 1
        num = polarity * int(''.join(digits))

        if num > max_int:
            num = max_int
        if num < min_int:
            num = min_int

        return num
