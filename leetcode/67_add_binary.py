# https://leetcode.com/problems/add-binary/

from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = '0'
        result = []
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            count = sum(bit == '1' for bit in [x, y, carry])
            if count == 3:
                result.append('1')
            elif count == 2:
                result.append('0')
                carry = '1'
            elif count == 1:
                result.append('1')
                carry = '0'
            else:
                result.append('0')

        if carry == '1':
            result.append('1')

        return ''.join(reversed(result))

    def addBinary(self, a: str, b: str) -> str:
        return f'{int(a, 2) + int(b, 2):>b}'

    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
