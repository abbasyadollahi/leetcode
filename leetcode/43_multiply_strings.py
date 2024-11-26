# https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str_int = dict(zip(map(str, range(10)), range(10)))

        digits1 = list(map(str_int.get, reversed(num1)))
        digits2 = list(map(str_int.get, reversed(num2)))
        product = [0] * (len(num1) + len(num2))

        for i, digit1 in enumerate(digits1):
            for j, digit2 in enumerate(digits2):
                product[i + j] += digit1 * digit2

        return str(sum(total * 10**i for i, total in enumerate(product)))
