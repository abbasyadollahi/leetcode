# https://www.hackerrank.com/x/library/hackerrank/all/questions/618520/view


def countAnalogousArrays(consecutiveDifference: list[int], lowerBound: int, upperBound: int) -> int:
    lowest = 0
    highest = 0
    total = 0

    for diff in consecutiveDifference:
        total += diff
        lowest = min(lowest, total)
        highest = max(highest, total)

    max_options = 1 + upperBound - lowerBound
    max_variance = highest - lowest
    possible_options = max_options - max_variance

    return max(possible_options, 0)
