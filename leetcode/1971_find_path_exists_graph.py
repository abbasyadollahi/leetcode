# https://leetcode.com/problems/find-if-path-exists-in-graph/

from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        connections = defaultdict(set)
        for edge in edges:
            u, v = edge
            connections[u].add(v)
            connections[v].add(u)

        visited = set()
        to_visit = [source]
        while to_visit:
            vertex = to_visit.pop()
            if vertex == destination:
                return True

            visited.add(vertex)
            to_visit.extend(connections[vertex] - visited)

        return False
