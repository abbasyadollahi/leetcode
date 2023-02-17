# https://www.hackerrank.com/x/library/hackerrank/all/questions/716477/view

import collections


def segment(x: int, space: list[int]) -> int:
    queue = collections.deque(maxlen=x)
    queue.extend(space[:x])

    mins = [min(queue)]
    for s in space[x:]:
        out = queue.popleft()
        queue.append(s)
        if out == mins[-1]:
            mins.append(min(queue))

    return max(mins)


def segment(x: int, space: list[int]) -> int:
    queue = collections.deque(maxlen=x)
    queue.extend(space[:x])

    i = x
    mins = [min(queue)]
    while i < len(space):
        new = space[i]
        out = queue.popleft()
        if new <= mins[-1]:
            queue.clear()
            queue.extend(space[i:i+x])
            mins.append(new)
            i += x
        elif out == mins[-1]:
            queue.append(new)
            mins.append(min(queue))
        else:
            queue.append(new)
        i += 1

    return max(mins)
