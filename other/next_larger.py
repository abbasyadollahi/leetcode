"""
Given a number, find the smallest number that's equal or larger with all neighboring digits being unique.

Input: 99
Output: 101
"""


import math


def num_to_digits(num: int) -> list[int]:
    return [(num // 10 ** i) % 10 for i in range(math.floor(math.log10(num)) + 1)]


def digits_to_num(digits: list[int]) -> int:
    return sum(digit * 10 ** i for i, digit in enumerate(digits))


def next_larger(num: int) -> int:
    digits = num_to_digits(num) + [0, 0]

    i = len(digits) - 2
    while i >= 0:
        if i > 0 and digits[i] == digits[i-1]:
            digits[i-1] += 1
            digits[i-1] %= 10
            digits[:i-1] = [0] * (i - 1)
            while digits[i-1] == 0:
                digits[i] += 1
                digits[i] %= 10
                i += 1
            if i > 0 and digits[i] == digits[i-1]:
                i += 1
        i -= 1

    return digits_to_num(digits)


assert next_larger(56) == 56
assert next_larger(1766) == 1767
assert next_larger(99) == 101
assert next_larger(44433) == 45010
assert next_larger(3299) == 3401
assert next_larger(100) == 101
