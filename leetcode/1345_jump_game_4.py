# https://leetcode.com/problems/jump-game-iv/

from collections import defaultdict


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        connected_indexes = defaultdict(list)
        for i, num in enumerate(arr):
            connected_indexes[num].append(i)
        for indexes in connected_indexes.values():
            indexes.sort(reverse=True)

        jumps = 0
        queue = [0]
        visited = set()
        while queue:
            next_queue = []
            for i in queue:
                if i == len(arr) - 1:
                    return jumps

                visited.add(i)

                next_queue.extend(
                    index
                    for index in connected_indexes[arr[i]]
                    if index not in visited
                )
                connected_indexes[arr[i]].clear()
                if i > 0 and i - 1 not in visited:
                    next_queue.append(i - 1)
                if i + 1 not in visited:
                    next_queue.append(i + 1)

            jumps += 1
            queue = next_queue

        return jumps
