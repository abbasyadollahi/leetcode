# https://www.hackerrank.com/x/library/hackerrank/all/questions/111168/view


def stockPairs(stocksProfit: list[int], target: int) -> int:
    count = {}
    for profit in stocksProfit:
        count[profit] = count.get(profit, 0) + 1

    distinct = 0
    half, odd = divmod(target, 2)
    if not odd and count.pop(half, 0) >= 2:
        distinct += 2

    for profit in count:
        diff = target - profit
        if diff in count:
            distinct += 1

    return distinct // 2
