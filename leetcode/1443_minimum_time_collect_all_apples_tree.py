# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

from collections import defaultdict, deque


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        apples = {i for i, has_apple in enumerate(hasApple) if has_apple}
        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)

        visited = {0}
        for apple in apples:
            queue = deque([(apple, set())])
            while queue:
                node, history = queue.popleft()
                if node in visited:
                    visited.update(history)
                    break
                else:
                    history.add(node)
                    queue.extend([(connection, history.copy()) for connection in connections[node] - history])

        return 2 * (len(visited) - 1)

    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        if not any(hasApple):
            return 0

        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)

        visited = set()

        def traverse(node: int) -> int:
            visited.add(node)
            count = sum(map(traverse, connections[node] - visited))

            if count or hasApple[node]:
                return count + 1
            else:
                return 0

        return 2 * (traverse(0) - 1)
