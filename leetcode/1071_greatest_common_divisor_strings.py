# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short_string = str1 if len(str1) < len(str2) else str2
        long_string = str1 if len(str1) >= len(str2) else str2

        for i in range(len(short_string), 0, -1):
            divisor = short_string[:i]
            if (
                len(short_string) % len(divisor) == 0 and
                len(long_string) % len(divisor) == 0 and
                short_string == divisor * (len(short_string) // len(divisor)) and
                long_string == divisor * (len(long_string) // len(divisor))
            ):
                return divisor

        return ''

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(x: int, y: int) -> int:
            return gcd(y, x % y) if x and y else x or y

        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1), len(str2))]
        else:
            return ''
