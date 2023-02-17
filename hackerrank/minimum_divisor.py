# https://www.hackerrank.com/x/library/hackerrank/all/questions/463595/view

import math


def minimumDivisor(arr: list[int], threshold: int) -> int:
    l = 1
    r = len(arr) * 10 ** 9
    while l <= r:
        m = (l + r) // 2
        total = sum(math.ceil(num / m) for num in arr)
        if total > threshold:
            l = m + 1
        else:
            r = m - 1

    return r + 1
