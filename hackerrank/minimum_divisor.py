# https://www.hackerrank.com/x/library/hackerrank/all/questions/463595/view

import math
from typing import List


def minimumDivisor(arr: List[int], threshold: int) -> int:
    l = 1
    r = len(arr) * 10 ** 9
    while l <= r:
        mid = (l + r) // 2
        total = sum(math.ceil(num / mid) for num in arr)
        if total > threshold:
            l = mid + 1
        else:
            r = mid - 1

    return r + 1
