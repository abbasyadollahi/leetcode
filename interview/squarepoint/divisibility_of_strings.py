import math


def findSmallestDivisor(s: str, t: str) -> int:
    def greatest_common_divisor(x: int, y: int) -> int:
        return greatest_common_divisor(y, x % y) if x and y else x or y

    if s + t == t + s:
        gcd = greatest_common_divisor(len(s), len(t))
        gcd_string = s[:gcd]
        for i in range(1, int(math.sqrt(gcd)) + 1):
            if gcd % i == 0 and (gcd // i) * gcd_string[:i] == gcd_string:
                return i
        return gcd
    else:
        return -1
