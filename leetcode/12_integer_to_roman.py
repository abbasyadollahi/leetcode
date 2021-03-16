# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        i2r = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            5000: '',
        }

        roman = ''
        divisor = 1000
        while divisor > 0:
            times = num // divisor
            if times == 9:
                roman += i2r[divisor] + i2r[divisor*10]
            elif times == 4:
                roman += i2r[divisor] + i2r[divisor*5]
            else:
                roman += i2r[divisor*5] * (times // 5) + i2r[divisor] * (times % 5)
            num %= divisor
            divisor //= 10

        return roman
