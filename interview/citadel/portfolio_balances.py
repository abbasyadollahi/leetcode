# https://www.hackerrank.com/x/library/hackerrank/all/questions/138976/view

def maxValue(n: int, rounds: list[int]) -> int:
    investments = [0] * n

    for left, right, contribution in rounds:
        investments[left-1] += contribution
        if right < n:
            investments[right] -= contribution

    for i in range(1, n):
        investments[i] += investments[i-1]

    return max(investments)
