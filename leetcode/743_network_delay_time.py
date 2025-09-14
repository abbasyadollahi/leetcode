# https://leetcode.com/problems/network-delay-time/

import heapq
import sys


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        delays = {}
        graph = [{} for _ in range(n + 1)]
        for source, destination, time in times:
            graph[source][destination] = time

        nodes = [(0, k)]
        while nodes:
            time, node = heapq.heappop(nodes)
            if node in delays:
                continue
            delays[node] = time
            for connection, delay in graph[node].items():
                heapq.heappush(nodes, (time + delay, connection))

        if len(delays) == n:
            return max(delays.values())
        else:
            return -1

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        max_delays = {}
        graph = [{} for _ in range(n + 1)]
        for source, destination, time in times:
            graph[source][destination] = time

        def traverse(node: int, time: int) -> None:
            max_delays[node] = min(max_delays.get(node, sys.maxsize), time)
            for connection, delay in graph[node].items():
                if time + delay < max_delays.get(connection, sys.maxsize):
                    traverse(connection, time + delay)

        traverse(k, 0)

        if len(max_delays) == n:
            return max(max_delays.values())
        else:
            return -1
