# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1
        carry = 0
        total = []
        while k != 0:
            digit = (num[i] if i >= 0 else 0) + (k % 10) + carry
            carry = digit // 10
            k //= 10
            i -= 1
            total.append(digit % 10)

        while i >= 0:
            digit = num[i] + carry
            carry = digit // 10
            i -= 1
            total.append(digit % 10)

        if carry:
            total.append(carry)

        return total[::-1]
