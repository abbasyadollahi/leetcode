# https://www.hackerrank.com/x/library/hackerrank/all/questions/466953/view


def droppedRequests(requestTime: list[int]) -> int:
    dropped = 0

    for i, time in enumerate(requestTime):
        if (
            (i >= 3 and time - 1 < requestTime[i - 3])
            or (i >= 20 and time - 10 < requestTime[i - 20])
            or (i >= 60 and time - 60 < requestTime[i - 60])
        ):
            dropped += 1

    return dropped
